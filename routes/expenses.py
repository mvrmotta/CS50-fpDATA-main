from forms.expense_form import ExpenseForm
from models import Expense, Category, Pet
from app import db
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

expenses = Blueprint('expenses', __name__)

@expenses.route('/add_expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    form = ExpenseForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    form.pet.choices = [(0, 'None')] + [(p.id, p.name) for p in Pet.query.all()]

    if form.validate_on_submit():
        pet_id = form.pet.data if form.pet.data != 0 else None

        expense = Expense(
            category_id=form.category.data,
            pet_id=pet_id,
            description=form.description.data,
            amount=form.amount.data,
            date=form.date.data,
            user_id=current_user.id
        )
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('expenses.list_expenses'))

    return render_template('add_expense.html', form=form)


@expenses.route('/list_expenses', methods=['GET'])
@login_required
def list_expenses():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template('list_expenses.html', expenses=expenses)

@expenses.route('/delete_expense/<int:expense_id>', methods=['POST'])
@login_required
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)

    if expense.user_id != current_user.id:
        flash("You cannot delete this Expense")
        return redirect(url_for('expenses.list_expenses'))

    db.session.delete(expense)
    db.session.commit()
    flash("Expense removed with success")
    return redirect(url_for('expenses.list_expenses'))
        