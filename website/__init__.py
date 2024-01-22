from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# initiating database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hdhdhshhshasha' #secret key for cookies 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #this is stating that the sql library is stored in the DB_NAME location which is in the website folder
    db.init_app(app) #initiating the db for this app

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') #/ is left empty otherwise it needs to be specified what the prefix is and it can become confusing

    from .models import User, Note

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    # Where teh user should be redirected if they have not logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id)) # Telling flask what user to look for

    return app

def create_database(app):
    # check if the db exists 
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app) #creates the db and we passing app 
        print('Created Database!')
