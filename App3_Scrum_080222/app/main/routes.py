from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    return render_template('index.html',  title='Home')
<<<<<<< Updated upstream
=======

@main.route('/contact', methods=['GET','POST'])
def contact(cat=None):
    return render_template('contact.html', title='Contact')

@main.route('/events', methods=['GET', 'POST'])
def events(cat=None):
    return render_template('events.html', title='Events')
>>>>>>> Stashed changes
