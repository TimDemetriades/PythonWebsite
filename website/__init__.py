from flask import Flask
from flask_sqlalchemy import SQLAlchemy    # for db
from os import path    # for checking if db has been created already
from flask_login import LoginManager    # for managing login related things

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random string'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'    # store db in website folder
    db.init_app(app)    # initialize db by giving it the flask app
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='')    # '' means no prefix
    app.register_blueprint(auth, url_prefix='')
    
    from .models import User, Note
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'    # where to redirect if user needs to login
    login_manager.init_app(app)    # tell login manager which app we are using
    
    # Tell flask how we load a user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))    # reference users by id (primary key)
    
    return app

def create_database(app):
    # Create db if it does not already exist
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Create database!')
    