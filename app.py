from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import database as db
import pandas as pd
import os
from translations import MESSAGES  # Import the translation dictionary

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'raseed_production_secret_key')

# Database Configuration
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///raseed_v2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_db(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for Flask-Login."""
    return db.User.query.get(int(user_id))

# --- Localization Logic ---

@app.before_request
def before_request():
    """Ensure a default language is set in the session."""
    if 'lang' not in session:
        session['lang'] = 'ar'  # Default to Arabic

@app.context_processor
def inject_content():
    """Inject translation dictionary and current language into all templates."""
    return dict(lang=session.get('lang', 'ar'), texts=MESSAGES)

@app.route('/set_lang/<lang_code>')
def set_language(lang_code):
    """Route to switch language between 'ar' and 'en'."""
    if lang_code in ['ar', 'en']:
        session['lang'] = lang_code
    return redirect(request.referrer or url_for('home'))

# --- Main Routes ---

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/dashboard')
@login_required
def dashboard():
    tenants, alerts = db.get_dashboard_data(current_user.id)
    return render_template('index.html', tenants=tenants, alerts=alerts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            # We will localize flash messages in a later push
            flash('Invalid email or password', 'danger')
            
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = db.User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered', 'danger')
            return redirect(url_for('signup'))
            
        new_user = db.User(name=name, email=email, password_hash=generate_password_hash(password))
        db.db.session.add(new_user)
        db.db.session.commit()
        
        login_user(new_user)
        return redirect(url_for('dashboard'))
        
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/add_tenant', methods=['POST'])
@login_required
def add_tenant():
    name = request.form.get('name')
    unit = request.form.get('unit')
    
    if db.add_tenant(current_user.id, name, unit):
        flash('Tenant added successfully', 'success')
    else:
        flash('Error: Tenant name already exists', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/tenant/<int:t_id>')
@login_required
def tenant_details(t_id):
    tenant, installments = db.get_tenant_details(t_id, current_user.id)
    if not tenant:
        flash('Access denied', 'danger')
        return redirect(url_for('dashboard'))
    return render_template('tenant.html', tenant=tenant, installments=installments)

@app.route('/upload_excel/<int:t_id>', methods=['POST'])
@login_required
def upload_excel(t_id):
    tenant, _ = db.get_tenant_details(t_id, current_user.id)
    if not tenant:
        return redirect(url_for('dashboard'))

    file = request.files['file']
    if file:
        try:
            df = pd.read_excel(file)
            df.columns = df.columns.str.strip().str.lower()
            
            date_col = next((c for c in df.columns if 'date' in c or 'تاريخ' in c), None)
            amount_col = next((c for c in df.columns if 'amount' in c or 'price' in c or 'مبلغ' in c), None)

            if date_col and amount_col:
                data_list = []
                for _, row in df.iterrows():
                    if pd.notna(row[date_col]) and pd.notna(row[amount_col]):
                        data_list.append((row[date_col], row[amount_col]))
                
                db.add_installments_from_excel(t_id, data_list)
                flash('Schedule uploaded successfully', 'success')
            else:
                flash('Invalid file format', 'danger')

        except Exception as e:
            flash(f'Error processing file: {e}', 'danger')
            
    return redirect(url_for('tenant_details', t_id=t_id))

@app.route('/pay/<int:inst_id>', methods=['POST'])
@login_required
def pay_installment(inst_id):
    paid_now = float(request.form['amount'])
    t_id = request.form['t_id']
    
    inst = db.Installment.query.get(inst_id)
    if inst:
        new_paid = inst.paid + paid_now
        db.update_installment(inst_id, paid=new_paid)
        
    flash('Payment recorded', 'success')
    return redirect(url_for('tenant_details', t_id=t_id))

@app.route('/update_total/<int:inst_id>', methods=['POST'])
@login_required
def update_total(inst_id):
    new_total = float(request.form['new_total'])
    t_id = request.form['t_id']
    
    db.update_installment(inst_id, amount=new_total)
    flash('Amount updated', 'info')
    return redirect(url_for('tenant_details', t_id=t_id))

@app.route('/delete_tenant/<int:t_id>')
@login_required
def delete_tenant(t_id):
    db.delete_tenant(t_id, current_user.id)
    flash('Record deleted', 'warning')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)