from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from sqlalchemy import func

db = SQLAlchemy()

class Tenant(db.Model):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    unit_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    installments = db.relationship('Installment', backref='tenant', cascade='all, delete-orphan')

    def to_dict(self):
        total = len(self.installments)
        completed = sum(1 for i in self.installments if (i.amount - i.paid) <= 0.1)
        return {
            'id': self.id,
            'name': self.name,
            'unit_name': self.unit_name,
            'total_installments': total,
            'completed_installments': completed
        }

class Installment(db.Model):
    __tablename__ = 'installments'
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Float, default=0.0)

    def to_dict(self):
        return {
            'id': self.id,
            'tenant_id': self.tenant_id,
            'due_date': self.due_date.strftime('%Y-%m-%d'),
            'amount': self.amount,
            'paid': self.paid
        }

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def add_tenant(name, unit):
    try:
        new_tenant = Tenant(name=name, unit_name=unit)
        db.session.add(new_tenant)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def get_dashboard_data():
    tenants_objs = Tenant.query.order_by(Tenant.created_at.desc()).all()
    tenants = [t.to_dict() for t in tenants_objs]
    
    target_date = datetime.now().date() + timedelta(days=15)
    
    upcoming_installments = db.session.query(Installment, Tenant).join(Tenant).filter(
        Installment.due_date <= target_date,
        (Installment.amount - Installment.paid) > 1
    ).order_by(Installment.due_date).all()
    
    alerts = []
    for inst, ten in upcoming_installments:
        alerts.append({
            'name': ten.name,
            'unit_name': ten.unit_name,
            'due_date': inst.due_date.strftime('%Y-%m-%d'),
            'remaining': inst.amount - inst.paid
        })
        
    return tenants, alerts

def delete_tenant(t_id):
    tenant = Tenant.query.get(t_id)
    if tenant:
        db.session.delete(tenant)
        db.session.commit()

def get_tenant_details(t_id):
    tenant_obj = Tenant.query.get(t_id)
    if not tenant_obj:
        return None, []
    
    inst_objs = Installment.query.filter_by(tenant_id=t_id).order_by(Installment.due_date).all()
    
    tenant = tenant_obj.to_dict()
    installments = [i.to_dict() for i in inst_objs]
    
    return tenant, installments

def add_installments_from_excel(tenant_id, data_list):
    for date_val, amount in data_list:
        if isinstance(date_val, str):
            date_obj = datetime.strptime(date_val, '%Y-%m-%d').date()
        elif isinstance(date_val, datetime):
            date_obj = date_val.date()
        else:
            continue
            
        new_inst = Installment(tenant_id=tenant_id, due_date=date_obj, amount=float(amount), paid=0)
        db.session.add(new_inst)
    db.session.commit()

def update_installment(inst_id, amount=None, paid=None):
    inst = Installment.query.get(inst_id)
    if inst:
        if amount is not None:
            inst.amount = amount
        if paid is not None:
            inst.paid = paid
        db.session.commit()