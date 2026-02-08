from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timedelta
from sqlalchemy.sql import func

db = SQLAlchemy()

# --- Models ---

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    tenants = db.relationship('Tenant', backref='landlord', lazy=True)

class Tenant(db.Model):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    unit_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    installments = db.relationship('Installment', backref='tenant', cascade="all, delete-orphan", lazy=True)

class Installment(db.Model):
    __tablename__ = 'installments'
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Float, default=0.0)

# --- Initialization ---

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

# --- Operations ---

def get_dashboard_data(user_id):
    """Fetch tenants and upcoming payment alerts for a specific user."""
    # 1. Get user's tenants with installment progress
    tenants = Tenant.query.filter_by(user_id=user_id).all()
    tenant_data = []
    
    for t in tenants:
        total_inst = len(t.installments)
        completed_inst = sum(1 for i in t.installments if i.paid >= i.amount)
        tenant_data.append({
            'id': t.id,
            'name': t.name,
            'unit_name': t.unit_name,
            'total_installments': total_inst,
            'completed_installments': completed_inst
        })

    # 2. Get alerts (payments due within 15 days)
    today = datetime.today().date()
    warning_date = today + timedelta(days=15)
    
    alerts_query = db.session.query(Installment, Tenant).join(Tenant).filter(
        Tenant.user_id == user_id,
        Installment.paid < Installment.amount,
        Installment.due_date <= warning_date
    ).all()

    alerts_data = [{
        'name': t.name,
        'unit_name': t.unit_name,
        'remaining': i.amount - i.paid,
        'due_date': i.due_date.strftime('%Y-%m-%d')
    } for i, t in alerts_query]

    return tenant_data, alerts_data

def get_financial_summary(user_id):
    """Calculate total paid and remaining amounts for the user's properties."""
    installments = db.session.query(Installment).join(Tenant).filter(Tenant.user_id == user_id).all()
    
    total_paid = 0
    total_remaining = 0

    for inst in installments:
        paid_val = inst.paid if inst.paid is not None else 0.0
        amount_val = inst.amount if inst.amount is not None else 0.0
        
        total_paid += paid_val
        total_remaining += (amount_val - paid_val)
    
    return {
        'total_paid': total_paid,
        'total_remaining': total_remaining
    }

def add_tenant(user_id, name, unit):
    """Add a new tenant if the name doesn't exist for this user."""
    existing = Tenant.query.filter_by(user_id=user_id, name=name).first()
    if existing:
        return False
    
    new_tenant = Tenant(user_id=user_id, name=name, unit_name=unit)
    db.session.add(new_tenant)
    db.session.commit()
    return True

def get_tenant_details(tenant_id, user_id):
    """Get tenant object and their installments securely."""
    tenant = Tenant.query.filter_by(id=tenant_id, user_id=user_id).first()
    if not tenant:
        return None, None
    
    installments_data = [{
        'id': i.id,
        'date': i.due_date.strftime('%Y-%m-%d'),
        'amount': i.amount,
        'paid': i.paid
    } for i in tenant.installments]
    
    # Sort by date
    installments_data.sort(key=lambda x: x['date'])
    
    return tenant, installments_data

def add_installments_from_excel(tenant_id, data_list):
    """Bulk add installments. data_list = [(date_str, amount), ...]"""
    for date_val, amount in data_list:
        try:
            # Handle various date formats potentially coming from Excel
            if isinstance(date_val, str):
                d_obj = datetime.strptime(date_val, '%Y-%m-%d').date()
            else:
                d_obj = date_val.date() # Assume it's a datetime object
            
            new_inst = Installment(tenant_id=tenant_id, due_date=d_obj, amount=float(amount))
            db.session.add(new_inst)
        except Exception as e:
            print(f"Skipping row due to error: {e}")
            continue
            
    db.session.commit()

def update_installment(inst_id, paid=None, amount=None):
    """Update payment or total amount for an installment."""
    inst = Installment.query.get(inst_id)
    if inst:
        if paid is not None:
            inst.paid = paid
        if amount is not None:
            inst.amount = amount
        db.session.commit()

def delete_tenant(tenant_id, user_id):
    """Delete a tenant and all associated data."""
    tenant = Tenant.query.filter_by(id=tenant_id, user_id=user_id).first()
    if tenant:
        db.session.delete(tenant)
        db.session.commit()