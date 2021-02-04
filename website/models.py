from . import db    # import from current package (folder) the db object
from flask_login import UserMixin    # gives user object login specific things
from sqlalchemy.sql import func    # gets current date for date column in note table

class Note(db.Model):    # inherits from db.Model
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

# User model db schema
class User(db.Model, UserMixin):    # inherits from db.Model and UserMixin
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))