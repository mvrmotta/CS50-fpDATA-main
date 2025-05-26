from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ExpenseForm(FlaskForm):
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    pet = SelectField('Pet', coerce=int, choices=[], validate_choice=False)
    description = StringField('Description', render_kw={"placeholder": "Enter the Expense's description"})
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0)], render_kw={"placeholder": "Enter the Expense's value in $"})
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Add Expense')
