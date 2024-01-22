# Storing standard roots for the website 
# Home page, Log in page, etc.
# Blueprint means it will have a bunch of routs inside
from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
@login_required
# The function runs when we at home page
def home():
    return render_template("home.html", user=current_user)
