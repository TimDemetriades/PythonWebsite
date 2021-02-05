from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User    # for adding user to db
from werkzeug.security import generate_password_hash, check_password_hash    # for hashing password
from . import db    # import from current package (folder) the db object
from flask_login import login_user, login_required, logout_user, current_user    # for handling logging in and out

auth = Blueprint('auth', __name__)    # blueprint for flask application


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if user is a valid user that's been created
        user = User.query.filter_by(email=email).first()
        if user:    # if a user with this email is found
            # Check if the password entered matches password hash stored
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)    # holds logged in user and stores in flask session
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
            
    return render_template("login.html")

@auth.route('/logout')
@login_required    # cannot access this page/route unless user is logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')
        
        user = User.query.filter_by(email=email).first()    # to check if user already exists
        
        if user:
            flash('Email already exists.', category='error')       
        elif len(email) < 4:
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
            login_user(user, remember=True)    # holds logged in user and stores in flask session
            return redirect(url_for('views.home'))    # views is blueprint, home is function within that blueprint (which contains the url)
            
    return render_template("sign_up.html")

