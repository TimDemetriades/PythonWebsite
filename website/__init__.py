from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
    
    return app