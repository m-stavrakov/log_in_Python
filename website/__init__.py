from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hdhdhshhshasha' #secret key for cookies 

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') #/ is left empty otherwise it needs to be specified what the prefix is and it can become confusing

    return app
