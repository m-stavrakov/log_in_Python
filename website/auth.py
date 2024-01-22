from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# GET and POST in method means that the py file will accept GET and POST requests from the html form 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # this will print ImmutableMultiDict([('email', 'tim@gmail.com'), ('password', 'hshhshsh')])
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Checking if the user exists in the db
        # Filtering through the User to check if the email exists and returns the first() result
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password): #Checks if the password of teh user is the same as the entered password
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required # This specifies that this page, route cannot be accessed unless the user is logged in 
def logout():
    # Logging out a user just using this method
    logout_user() 
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Getting the information from the form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error') 
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # defining the user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            # adding the user to the database
            db.session.add(new_user)
            # making a commit to the database
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)