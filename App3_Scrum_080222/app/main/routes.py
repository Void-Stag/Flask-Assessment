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
    return render_template('/Course/course.html', title='Courses')

@main.route('/home', methods=['GET', 'POST'])
def home(cat=None):
    return render_template('home.html', title='Home')

@main.route('/users', methods=['GET','POST'])
def users(cat=None):
        return render_template('/Course/certiuse.html', title='Users')

@main.route('/faq', methods=['GET','POST'])
def faq(cat=None):
    return render_template('FAQ.html', title='FAQ')

@main.route('/improvements', methods=['GET','POST'])
def improvements(cat=None):
    return render_template('Improvements.html', title='Improvements')

@main.route('/basicscrum', methods=['GET', 'POST'])
def basicscrum(cat=None):
    return render_template('/Course/SCRUM_basics.html', title='Scrum Basics')

@main.route('/addcourse', methods=['GET', 'POST'])
def addcourse(cat=None):
    return render_template('/Course/additionalcourses.html', title='Additional Courses')
    
@main.route('/jobs', methods=['GET', 'POST'])
def jobs(cat=None):
    return render_template('/Member_Only/jobs.html', title='Jobs')    

@main.route('/userstories_acceptancecriteria', methods=['GET', 'POST'])
def userstories_acceptancecriteria(cat=None):
    return render_template('/Course/course_post/usercriteria.html', title='User Stories & Acceptance Criteria')

@main.route('/burnout_charts', methods=['GET', 'POST'])
def burnout_charts(cat=None):
    return render_template('/Course/course_post/burnoutchart.html', title='Burnout Charts for Dummies')

@main.route('/dev_cycles', methods=['GET', 'POST'])
def dev_cycles(cat=None):
    return render_template('/Course/course_post/devcycles.html', title='Different types of Development Cycles')
    
@main.route('/scrum_project', methods=['GET', 'POST'])
def scrum_project(cat=None):
    return render_template('/Course/course_post/scrumweb.html', title='SCRUM Website Project')

@main.route('/member_articles', methods=['GET', 'POST'])
def member_articles(cat=None):
    return render_template('/Member_Only/memberarticle.html', title='Member Articles')

@main.route('/welcome_member', methods=['GET', 'POST'])
def welcome_member(cat=None):
    return render_template('/Member_Only/article/memberwelcome.html', title='Welcome Member')

@main.route('/cookie_policy', methods=['GET', 'POST'])
def cookie_policy(cat=None):
    return render_template('/Legal/cookie_policy.html', title='Cookie Policy')

@main.route('/Jane_Dane', methods=['GET', 'POST'])
def Jane_Dane(cat=None):
    return render_template('/Trainer_Profile/Jane_Prof.html', title='Jane Dane')

@main.route('/John_Doe', methods=['GET', 'POST'])
def John_Doe(cat=None):
    return render_template('/Trainer_Profile/John_Prof.html', title='John Doe')