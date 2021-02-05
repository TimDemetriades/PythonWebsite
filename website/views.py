from flask import Blueprint, render_template
from flask_login import login_required, current_user    # for handling logging in and out

views = Blueprint('views', __name__)    # blueprint for flask application


@views.route('/')
@login_required    # cannot access this page/route unless user is logged in
def home():
    # return "<h1>Tim Test</h1>"
    return render_template("home.html")