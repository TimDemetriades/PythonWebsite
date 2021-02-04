from flask import Flask
from flask_sqlalchemy import SQLAlchemy    # for db
from os import path    # for checking if db has been created already

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
    
    return app

def create_database(app):
    # Create db if it does not already exist
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Create database!')
    