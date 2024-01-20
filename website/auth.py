from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

# GET and POST in method means that the py file will accept GET and POST requests from the html form 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # this will print ImmutableMultiDict([('email', 'tim@gmail.com'), ('password', 'hshhshsh')])
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p> logout </p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Getting the information from the form
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error') 
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("sign_up.html")