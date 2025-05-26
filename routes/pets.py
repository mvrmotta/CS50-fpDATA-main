from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from models import Pet
from forms.pet_form import PetForm
from flask_login import login_required, current_user

pets = Blueprint('pets', __name__)

@pets.route('/add_pet', methods=['GET', 'POST'])
@login_required
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            breed=form.breed.data,
            birth_date=form.birth_date.data,
            weight=form.weight.data,
            user_id=current_user.id
        )
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('pets.list_pets'))

    return render_template('add_pet.html', form=form)


@pets.route('/list_pets', methods=['GET'])
@login_required
def list_pets():
    pets = Pet.query.filter_by(user_id=current_user.id).all()
    return render_template('list_pets.html', pets=pets)

@pets.route('/delete_pet/<int:pet_id>', methods=['POST'])
@login_required
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)

    if pet.user_id != current_user.id:
        flash("You cannot delete this Pet")
        return redirect(url_for('pets.list_pets'))
    
    db.session.delete(pet)
    db.session.commit()
    flash("Pet removed with success")
    return redirect(url_for('pets.list_pets'))