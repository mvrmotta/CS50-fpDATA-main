from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from models import User
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from app import db

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.hash, form.password.data):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home'))

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        flash('User registered successfully!')
        return redirect(url_for('home'))

    return render_template('register.html', form=form)

"""@users.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')"""
