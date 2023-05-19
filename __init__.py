# the __init__.py file makes the website file a python package in the directory

from flask import Flask


def create_app():

    app = Flask(__name__)  # initializes the flask app
    app.config['SECRET KEY'] = 'createPasswordLater'  # encrypts the cookie data -- the key is the password for the site

    from .views import views  # tells Python we have Blueprints for the application
    app.register_blueprint(views, url_prefix='/')  # registers the blueprints with the flask app
    # url tells where to access all the blueprints pages within the url

    return app
