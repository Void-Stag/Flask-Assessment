from flask import Blueprint, render_template, redirect, url_for, request
from app.models import db, Announcement
from flask import jsonify

main = Blueprint('main', __name__)
#

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

@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home(cat=None):
  #  announcement = Announcement.query.all()
    return render_template('home.html', title='Home',) #announcement=announcement)

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

@main.route('/cookie_policy', methods=['GET', 'POST'])
def cookie_policy(cat=None):
    return render_template('/Legal/cookie_policy.html', title='Cookie Policy')

@main.route('/Jane_Dane', methods=['GET', 'POST'])
def Jane_Dane(cat=None):
    return render_template('/Trainer_Profile/Jane_Prof.html', title='Jane Dane')

@main.route('/John_Doe', methods=['GET', 'POST'])
def John_Doe(cat=None):
    return render_template('/Trainer_Profile/John_Prof.html', title='John Doe')

@main.route('/articles', methods=['GET', 'POST'])
def articles(cat=None):
    return render_template('/Articles/Articles.html', title='Articles')

@main.route('/whatnext', methods=['GET', 'POST'])
def whatnext(cat=None):
    return render_template('/Articles/Article#1.html', title='What is next?')

#Announcement database routes
@main.route('/getannounce', methods=['GET', 'POST'])
def getannounce(cat=None):
    print(f"announcements {cat}")
    toReturn= ('banana ', 'blinky ', 'pie ')
    return jsonify(toReturn) #Returns declared values for json

#@main.route('/addannounce', methods=['POST'])
#def addannounce():
   # content = request.form.get('content')
    #title = request.form.get('title')
    #if title != '' and content!= '' != None:
     #   p = Announcement(title=title, content=content)
      #  db.session.add(p)
       # db.session.commit()
       # return redirect('/')
   # else:
    #    return redirect('/')



#Users
@main.route('/jobs', methods=['GET','POST'])
def jobs(cat=None):
    return render_template('/User_Only/jobs.html', title='Jobs')

#Members
@main.route('/member_articles', methods=['GET', 'POST'])
def member_articles(cat=None):
    return render_template('/Articles/memberarticle.html', title='Member Articles')

@main.route('/welcome_member', methods=['GET', 'POST'])
def welcome_member(cat=None):
    return render_template('/Articles/Member_Only/memberwelcome.html', title='Welcome Member')
#Trainers

#Admin



































@main.route('/privacy_policy', methods=['GET','POST'])
def privacy_policy(cat=None):
    return render_template('/Legal/privacy_policy.html', title='Privacy Policy')