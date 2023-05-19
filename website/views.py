# views stores the standard routes for the website (any page user can visit)

from flask import Blueprint
from flask import render_template  # how to load a html template
from flask import url_for
from flask import request
from flask import flash  # displays messages to the user

views = Blueprint('views', __name__)  # sets up a blueprint for the flask application


@views.route('/')
def home():
    return render_template('bootstrapIndex.html')


@views.route('/services')
def services():
    return render_template('services.html')
