from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User

main = Blueprint('main', __name__)

users = [
            {"id": 1, "name": "Jane Dane", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "John Doe", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
        ]


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



@main.route("/User/<int:user_id>")
def user_details(user_id):
    """View function for Showing Details of Each Pet.""" 
    user = next((user for user in users if user["id"] == user_id), None) 
    if user is None: 
        abort(404, description="No User was Found with the given ID")
    return render_template("User.html", user = user)