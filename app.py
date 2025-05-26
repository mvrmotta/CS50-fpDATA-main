from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# For this project I used the help of AI to brainstorm about ideas that would fit me, 
# also as a teacher for libraries and extensions that i didn't know how to use, and for debugging errors that were generated
# from content I was not used to see in CS50 problem sets. Also used for upgrading my knowledge in modularizing the Flask application 

# 1. Cria o app
app = Flask(__name__)

# 2. Configurações
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance_pet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'


# 3. Inicializa o banco
db = SQLAlchemy(app)

# 4. Inicializa o Migrate
migrate = Migrate(app, db)

# 5. Importa modelos DEPOIS de db estar criado
from models import User, Pet, Category, Expense

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.init_app(app)

# User Loader

from models import User
from flask_login import login_user, logout_user, login_required, current_user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Rota básica
@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.show_dashboard'))
    return render_template("home.html")

from routes.pets import pets
from routes.expenses import expenses
from routes.users import users
from routes.dashboard import dashboard

app.register_blueprint(pets)
app.register_blueprint(expenses)
app.register_blueprint(users)
app.register_blueprint(dashboard)


if __name__ == "__main__":
    app.run(debug=True)
