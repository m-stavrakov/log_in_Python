# Storing standard roots for the website 
# Home page, Log in page, etc.
# Blueprint means it will have a bunch of routs inside
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
# The function runs when we at home page
def home():
    return render_template("home.html")
