from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import Expense, Category
from app import db
from sqlalchemy import func
from datetime import datetime
from models import Pet

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/dashboard')
@login_required
def show_dashboard():

    # Mês atual
    current_month = datetime.now().strftime('%Y-%m')

    total_current_month = db.session.query(
        func.sum(Expense.amount)
    ).filter(
        Expense.user_id == current_user.id,
        func.strftime('%Y-%m', Expense.date) == current_month
    ).scalar() or 0

    # Total gasto geral
    total_all = db.session.query(
        func.sum(Expense.amount)
    ).filter_by(user_id=current_user.id).scalar() or 0

    category_max = db.session.query(
        Category.name,
        func.sum(Expense.amount).label('total')
    ).join(Expense).filter(
        Expense.user_id == current_user.id
    ).group_by(Category.name).order_by(func.sum(Expense.amount).desc()).first()

    category_max_name = category_max[0] if category_max else None
    category_max_value = category_max[1] if category_max else 0

    

    pet_max = db.session.query(
        Pet.name,
        func.sum(Expense.amount).label('total')
    ).join(Expense).filter(
        Expense.user_id == current_user.id
    ).group_by(Pet.name).order_by(func.sum(Expense.amount).desc()).first()

    pet_max_name = pet_max[0] if pet_max else None
    pet_max_value = pet_max[1] if pet_max else 0



    # Número de meses distintos com gasto
    months_with_expenses = db.session.query(
        func.strftime('%Y-%m', Expense.date)
    ).filter_by(user_id=current_user.id).distinct().count()

    # Média
    avg_per_month = total_all / months_with_expenses if months_with_expenses else 0


    # Total gasto
    total_expenses = db.session.query(
        func.sum(Expense.amount)
    ).filter_by(user_id=current_user.id).scalar() or 0

    # Gastos por categoria e mês
    data = db.session.query(
        func.strftime('%Y-%m', Expense.date).label('month'),
        Category.name,
        func.sum(Expense.amount)
    ).join(Category).filter(
        Expense.user_id == current_user.id
    ).group_by('month', Category.name).order_by('month').all()

    # Estrutura: { categoria: { mês: valor } }
    result = {}

    for month, category, amount in data:
        result.setdefault(category, {})[month] = float(amount)

    # Listar todos os meses presentes → para o eixo X
    all_months = sorted({month for month, _, _ in data})

    print(f"Total: {total_expenses}, Data: {result}, Meses: {all_months}")

    return render_template('dashboard.html', total=total_expenses, data=result, months=all_months, total_current_month=total_current_month, 
                           avg_per_month=avg_per_month, category_max_name=category_max_name, category_max_value=category_max_value,
                           pet_max_name=pet_max_name, pet_max_value=pet_max_value)

