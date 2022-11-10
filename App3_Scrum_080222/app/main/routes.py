from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    return render_template('index.html',  title='Home')

@main.route('/contact', methods=['GET','POST'])
def contact(cat=None):
    return render_template('contact.html', title='Contact')

@main.route('/events', methods=['GET','POST'])
def events(cat=None):
    return render_template('event.html', title='Events')

@main.route('/sitemap', methods=['GET', 'POST'])
def sitemap(cat=None):
    return render_template('sitemap.html', title='SiteMap')

@main.route('/course', methods=['GET', 'POST'])
def course(cat=None):
    return render_template('course.html', title='Courses')

@main.route('/home', methods=['GET', 'POST'])
def home(cat=None):
    return render_template('home.html', title='Home')

@main.route('/users', methods=['GET','POST'])
def users(cat=None):
        return render_template('certiuse.html', title='Users')