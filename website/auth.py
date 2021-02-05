from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User    # for adding user to db
from werkzeug.security import generate_password_hash, check_password_hash    # for hashing password
from . import db    # import from current package (folder) the db object

auth = Blueprint('auth', __name__)    # blueprint for flask application


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password != passwordConfirm:
            flash('Passwords must match.', category='error')
        elif len(password) < 7:
            flash('Password must be longer than 6', category='error')
        else:
            # add user to db
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))    # views is blueprint, home is function within that blueprint (which contains the url)
            
    return render_template("sign_up.html")

