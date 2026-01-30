from flask import Flask, render_template, request, redirect, url_for, flash
import database as db
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "raseed_production_secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///real_estate.db2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_db(app)

# --- Temporary Dummy User ID for Testing (Push 2) ---
# Will be replaced by 'current_user.id' in Push 3
TEMP_USER_ID = 1

@app.route('/')
def index():
    tenants, alerts = db.get_dashboard_data(TEMP_USER_ID)
    return render_template('index.html', tenants=tenants, alerts=alerts)

@app.route('/add_tenant', methods=['POST'])
def add_tenant():
    name = request.form.get('name')
    unit = request.form.get('unit')
    
    if db.add_tenant(TEMP_USER_ID, name, unit):
        flash('تم إضافة المستأجر بنجاح', 'success')
    else:
        flash('خطأ: اسم المستأجر موجود مسبقاً', 'danger')
    return redirect(url_for('index'))

@app.route('/tenant/<int:t_id>')
def tenant_details(t_id):
    # Pass user_id to ensure ownership
    tenant, installments = db.get_tenant_details(t_id, TEMP_USER_ID)
    if not tenant:
        flash('غير مصرح لك بالوصول لهذا الملف', 'danger')
        return redirect(url_for('index'))
    return render_template('tenant.html', tenant=tenant, installments=installments)

@app.route('/upload_excel/<int:t_id>', methods=['POST'])
def upload_excel(t_id):
    # Verify ownership first
    tenant, _ = db.get_tenant_details(t_id, TEMP_USER_ID)
    if not tenant:
        return redirect(url_for('index'))

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
                flash('تم رفع جدول الدفعات بنجاح', 'success')
            else:
                flash('الملف لا يحتوي على الأعمدة المطلوبة', 'danger')

        except Exception as e:
            flash(f'حدث خطأ أثناء المعالجة: {e}', 'danger')
            
    return redirect(url_for('tenant_details', t_id=t_id))

@app.route('/pay/<int:inst_id>', methods=['POST'])
def pay_installment(inst_id):
    paid_now = float(request.form['amount'])
    t_id = request.form['t_id']
    
    # Simple check, full verification in next push
    db.update_installment(inst_id, paid=db.Installment.query.get(inst_id).paid + paid_now)
        
    flash('تم تسجيل الدفعة بنجاح', 'success')
    return redirect(url_for('tenant_details', t_id=t_id))

@app.route('/update_total/<int:inst_id>', methods=['POST'])
def update_total(inst_id):
    new_total = float(request.form['new_total'])
    t_id = request.form['t_id']
    
    db.update_installment(inst_id, amount=new_total)
    flash('تم تحديث قيمة العقد', 'info')
    return redirect(url_for('tenant_details', t_id=t_id))

@app.route('/delete_tenant/<int:t_id>')
def delete_tenant(t_id):
    db.delete_tenant(t_id, TEMP_USER_ID)
    flash('تم حذف السجل نهائياً', 'warning')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)