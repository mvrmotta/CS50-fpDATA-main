import sys
import os

# Ajusta o sys.path para encontrar app e models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import db, app
from models import Category

CATEGORIES = [
    'Alimentação',
    'Veterinário',
    'Higiene',
    'Brinquedos',
    'Transporte',
    'Outros'
]

def seed_categories():
    for name in CATEGORIES:
        exists = Category.query.filter_by(name=name).first()
        if not exists:
            category = Category(name=name)
            db.session.add(category)
    db.session.commit()
    print("Categorias inseridas com sucesso!")

if __name__ == "__main__":
    with app.app_context():
        seed_categories()
