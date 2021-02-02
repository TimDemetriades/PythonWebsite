from flask import Blueprint

views = Blueprint('views', __name__)    # blueprint for flask application


@views.route('/')
def home():
    return "<h1>Tim Test</h1>"