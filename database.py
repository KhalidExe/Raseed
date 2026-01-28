import sqlite3
from datetime import datetime, timedelta

DB_NAME = "real_estate.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # <--- هذا السطر هو الحل السحري
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tenants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE,
                    unit_name TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS installments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tenant_id INTEGER,
                    due_date DATE,
                    amount REAL,
                    paid REAL DEFAULT 0,
                    FOREIGN KEY(tenant_id) REFERENCES tenants(id) ON DELETE CASCADE
                )''')
    conn.commit()
    conn.close()

def add_tenant(name, unit):
    try:
        conn = get_db()
        conn.execute("INSERT INTO tenants (name, unit_name) VALUES (?, ?)", (name, unit))
        conn.commit()
        conn.close()
        return True
    except:
        return False

def get_dashboard_data():
    conn = get_db()
    # جلب البيانات وتحويلها لقواميس
    rows = conn.execute("""
        SELECT t.*, 
        (SELECT COUNT(*) FROM installments WHERE tenant_id=t.id) as total_installments,
        (SELECT COUNT(*) FROM installments WHERE tenant_id=t.id AND (amount-paid) <= 0.1) as completed_installments
        FROM tenants t
        ORDER BY t.created_at DESC
    """).fetchall()
    
    tenants = [dict(row) for row in rows] # <--- تحويل النتائج
    
    # جلب التنبيهات
    target_date = (datetime.now() + timedelta(days=15)).strftime("%Y-%m-%d")
    alert_rows = conn.execute("""
        SELECT t.name, t.unit_name, i.due_date, (i.amount - i.paid) as remaining
        FROM installments i 
        JOIN tenants t ON i.tenant_id = t.id
        WHERE i.due_date <= ? AND (i.amount - i.paid) > 1
        ORDER BY i.due_date ASC
    """, (target_date,)).fetchall()
    
    alerts = [dict(row) for row in alert_rows] # <--- تحويل النتائج
    
    conn.close()
    return tenants, alerts

def delete_tenant(t_id):
    conn = get_db()
    conn.execute("DELETE FROM tenants WHERE id=?", (t_id,))
    conn.commit()
    conn.close()

def get_tenant_details(t_id):
    conn = get_db()
    tenant_row = conn.execute("SELECT * FROM tenants WHERE id=?", (t_id,)).fetchone()
    tenant = dict(tenant_row) if tenant_row else None
    
    inst_rows = conn.execute("SELECT * FROM installments WHERE tenant_id=? ORDER BY due_date ASC", (t_id,)).fetchall()
    installments = [dict(row) for row in inst_rows]
    
    conn.close()
    return tenant, installments

def add_installments_from_excel(tenant_id, data_list):
    conn = get_db()
    for date_val, amount in data_list:
        if isinstance(date_val, datetime):
            d_str = date_val.strftime("%Y-%m-%d")
        else:
            d_str = str(date_val).split(" ")[0]
        conn.execute("INSERT INTO installments (tenant_id, due_date, amount, paid) VALUES (?, ?, ?, 0)",
                     (tenant_id, d_str, float(amount)))
    conn.commit()
    conn.close()

def update_installment(inst_id, amount=None, paid=None):
    conn = get_db()
    if amount is not None:
        conn.execute("UPDATE installments SET amount=? WHERE id=?", (amount, inst_id))
    if paid is not None:
        conn.execute("UPDATE installments SET paid=? WHERE id=?", (paid, inst_id))
    conn.commit()
    conn.close()