from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hash = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    pets = db.relationship('Pet', backref='owner', lazy=True)
    expenses = db.relationship('Expense', backref='user', lazy=True)