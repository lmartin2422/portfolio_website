# views stores the standard routes for the website (any page user can visit)

from flask import Blueprint  # Importing the Blueprint class from Flask, used to organize your application into smaller components (ex: views, templates, and static files, among other things.)
from flask import render_template  # Importing the render_template function, used to load an HTML template
from flask import url_for  # Importing the url_for function, used to generate URLs for a specific function
from flask import request  # Importing the request object, used to handle incoming requests
from flask import flash  # Importing the flash function, used to display messages to the user


views = Blueprint('views', __name__)  # sets up a blueprint for the flask application


@views.route('/')
def home():
    return render_template('bootstrapIndex.html')


@views.route('/services')
def services():
    return render_template('services.html')
