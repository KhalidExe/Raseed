from flask import Flask, render_template, request, redirect, url_for, flash
import database as db
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "raseed_app_secure_key"

# Initialize Database on startup
db.init_db()

@app.route('/')
def index():
    """Render Dashboard"""
    tenants, alerts = db.get_dashboard_data()
    return render_template('index.html', tenants=tenants, alerts=alerts)

@app.route('/add_tenant', methods=['POST'])
def add_tenant():
    """Add new tenant to database"""
    name = request.form.get('name')
    unit = request.form.get('unit')
    
    if db.add_tenant(name, unit):
        flash('تم إضافة المستأجر بنجاح', 'success')
    else:
        flash('خطأ: الاسم موجود مسبقاً', 'danger')
    return redirect(url_for('index'))

@app.route('/tenant/<int:t_id>')
def tenant_details(t_id):
    """Render tenant details and ledger"""
    tenant, installments = db.get_tenant_details(t_id)
    return render_template('tenant.html', tenant=tenant, installments=installments)

@app.route('/upload_excel/<int:t_id>', methods=['POST'])
def upload_excel(t_id):
    """Handle Excel file upload"""
    file = request.files['file']
    if file:
        try:
            df = pd.read_excel(file)
            # Normalize column names
            df.columns = df.columns.str.strip().str.lower()
            
            # Detect columns dynamically
            date_col = next((c for c in df.columns if 'date' in c or 'تاريخ' in c), df.columns[0])
            amount_col = next((c for c in df.columns if 'amount' in c or 'price' in c or 'مبلغ' in c), df.columns[1])

            data_list = []
            for _, row in df.iterrows():
                if pd.notna(row[date_col]) and pd.notna(row[amount_col]):
                    data_list.append((row[date_col], row[amount_col]))
            
            db.add_installments_from_excel(t_id, data_list)
            flash('تم رفع الجدول بنجاح', 'success')
        except Exception as e:
            flash(f'خطأ في الملف: {e}', 'danger')
            
    return redirect(url_for('tenant_details', t_id=t_id))

@app.route('/pay/<int:inst_id>', methods=['POST'])
def pay_installment(inst_id):
    """Process payment"""
    paid_now = float(request.form['amount'])
    t_id = request.form['t_id']
    
    conn = db.get_db()
    row = conn.execute("SELECT paid FROM installments WHERE id=?", (inst_id,)).fetchone()
    if row:
        new_paid = row['paid'] + paid_now
        db.update_installment(inst_id, paid=new_paid)
        conn.close()
    
    flash('تم تسجيل الدفعة', 'success')
    return redirect(url_for('tenant_details', t_id=t_id))

@app.route('/update_total/<int:inst_id>', methods=['POST'])
def update_total(inst_id):
    """Update contract total for an installment"""
    new_total = float(request.form['new_total'])
    t_id = request.form['t_id']
    db.update_installment(inst_id, amount=new_total)
    flash('تم تعديل قيمة العقد', 'info')
    return redirect(url_for('tenant_details', t_id=t_id))

@app.route('/delete_tenant/<int:t_id>')
def delete_tenant(t_id):
    """Delete tenant permanently"""
    db.delete_tenant(t_id)
    flash('تم حذف المستأجر', 'warning')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)