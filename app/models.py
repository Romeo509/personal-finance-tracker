from flask_login import UserMixin
from app import login_manager, db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    expenses = db.relationship('Expense', backref='user', lazy=True)

    def add_expense(self, amount, category, description=None):
        expense = Expense(amount=amount, category=category, description=description, user=self)
        db.session.add(expense)
        db.session.commit()

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Keep your initial user_loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
