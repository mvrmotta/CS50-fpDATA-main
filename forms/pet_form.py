from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange, ValidationError

class PetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Enter the pet's name"})
    species = StringField('Species', validators=[DataRequired()], render_kw={"placeholder": "Enter the pet's species (Dog, Cat, Turtle...)"})
    breed = StringField('Breed', render_kw={"placeholder": "Enter the pet's breed"})
    birth_date = DateField('Birth Date', format='%Y-%m-%d')
    weight = StringField('Weight', render_kw={"placeholder": "Enter the pet's weight in Kg"}, validators=[
        InputRequired(message='Enter the Weight.')
    ])
    submit = SubmitField('Add Pet')

    def validate_weight(form, field): # type: ignore
        data = str(field.data).lower().replace('kg', '').strip()
        data = data.replace(',', '.')
        try:
            weight_float = float(data)
            if weight_float < 0:
                raise ValidationError('Weight must be positive.')
            field.data = weight_float  # Armazena como float para o banco
        except ValueError:
            raise ValidationError('Please enter a valid weight (ex.: 12 ou 12,5 ou 12kg).')
