from app import db

class Pet(db.Model):
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(30), nullable=False)
    breed = db.Column(db.String(50))
    birth_date = db.Column(db.Date)
    weight = db.Column(db.Float)

    expenses = db.relationship('Expense', backref='pet', lazy=True)