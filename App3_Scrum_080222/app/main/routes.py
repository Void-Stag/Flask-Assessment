from flask import Blueprint, render_template, redirect, url_for, request
from app.models import db, Announcement
from flask import jsonify

main = Blueprint('main', __name__)
#
@main.route('/events', methods=['GET','POST'])# Defines the route name and what it can do. GET is fetching data and POST is sending data
def events(cat=None):#Function defines what happens when the route is called
    return render_template('event.html', title='Events')#Returns the html file which is rendered to display data using jinja as it is a child template file

@main.route('/sitemap', methods=['GET', 'POST'])
def sitemap(cat=None):
    return render_template('sitemap.html', title='SiteMap')

@main.route('/course', methods=['GET', 'POST'])
def course(cat=None):
    return render_template('/Course/course.html', title='Courses')

@main.route('/')
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

# Map & Contact Pages
@main.route('/Map', methods=['GET', 'POST'])
def Map(cat=None):
    return render_template('/Contact and Map/Map.html', title='Map')

@main.route('/Contact', methods=['GET', 'POST'])
def Contact(cat=None):
    return render_template('/Contact and Map/Contact.html', title='Contact')

#Certification Courses
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

#Non certification Courses
@main.route('/python_basics', methods=['GET', 'POST'])
def python_basics(cat=None):
    return render_template('/Course/addcourse/pythonbasic.html', title='Python Basics')

#Legal
@main.route('/cookie_policy', methods=['GET', 'POST'])
def cookie_policy(cat=None):
    return render_template('/Legal/cookie_policy.html', title='Cookie Policy')

# Trainer Profiles
@main.route('/Jane_Dane', methods=['GET', 'POST'])
def Jane_Dane(cat=None):
    return render_template('/Trainer_Profile/Jane_Prof.html', title='Jane Dane')

@main.route('/John_Doe', methods=['GET', 'POST'])
def John_Doe(cat=None):
    return render_template('/Trainer_Profile/John_Prof.html', title='John Doe')

# Practitioner Profiles
@main.route('/Heather_Smith', methods=['GET','POST'])
def Heather_Smith(cat=None):
    return render_template('/Practitioner_Profile/Heather_Prof.html', title='Heather Smith')

@main.route('/Sagar_Kesh', methods=['GET','POST'])
def Sagar_Kesh(cat=None):
    return render_template('/Practitioner_Profile/Sagar_Prof.html', title='Sagar Keshawala')

@main.route('/Marcus_Yidom', methods=['GET','POST'])
def Marcus_Yidom(cat=None):
    return render_template('/Practitioner_Profile/Marcus_Prof.html', title='Marcus Yidom')

# Master Profiles
@main.route('/Wallace_Harrison', methods=['GET','POST'])
def Wallace_Harrison(cat=None):
    return render_template('/Master_Profile/Wallace_Prof.html', title='Wallace Harrison')

#Articles
@main.route('/articles', methods=['GET', 'POST'])
def articles(cat=None):
    return render_template('/Articles/Articles.html', title='Articles')

@main.route('/whatnext', methods=['GET', 'POST'])
def whatnext(cat=None):
    return render_template('/Articles/Article#1.html', title='What is next?')

#Announcement database routes
@main.route('/getannounce', methods=['GET', 'POST'])
def getannounce(cat=None):
    announcement = [] # Declare an empty list
    for row in Announcement.query.all(): # gathers all the data in the Announcement table
        announcement.append((str(row.title), str(row.content)))# Turns the table data into strings
        #print(f"announcements {announcement}") Debugging code
    #toReturn= ('banana ', 'blinky ', 'pie ') Debugging code
    return jsonify(announcement) #Returns declared values for json

@main.route('/addannounce', methods=['POST'])
def addannounce():
    content = request.form.get('content')# Requests the values in the title box
    title = request.form.get('title')#Requests the values in the content box
    #print("announce 1") Debugging code
    if title != '' and content!= '' != None: # If there is content in the form boxes then the following with execute
       # print("announce 2") Debugging code
        p = Announcement(title=title, content=content)# finds the declared tables to put the values into
        db.session.add(p)# Adds the requested values to the declared fields
        db.session.commit()# saves the database
        #print("announce 3") Debugging code
   #print("announce 4") Debugging code
    return redirect('/')#Refreshes the page


#Jobs
@main.route('/jobs', methods=['GET','POST'])
def jobs(cat=None):
    return render_template('/User_Only/jobs.html', title='Jobs')

#Member Articles
@main.route('/member_articles', methods=['GET', 'POST'])
def member_articles(cat=None):
    return render_template('/Articles/memberarticle.html', title='Member Articles')

@main.route('/welcome_member', methods=['GET', 'POST'])
def welcome_member(cat=None):
    return render_template('/Articles/Member_Only/memberwelcome.html', title='Welcome Member')

#Trainers
#Trainer Info
@main.route('/trainer_info', methods=['GET', 'POST'])
def trainer_info(cat=None):
    return render_template('/Course/trainerinfo.html', title='Trainer Info ')

@main.route('/new_course', methods=['GET', 'POST'])
def new_course(cat=None):
    return render_template('/Course/traininfo/addnewcourse.html', title='Add New Course')
#Admin


#Current User Profile
@main.route('/profile', methods=['GET', 'POST'])
def profile(cat=None):
    return render_template('/User_Only/Profile.html', title='Profile')
































@main.route('/privacy_policy', methods=['GET','POST'])
def privacy_policy(cat=None):
    return render_template('/Legal/privacy_policy.html', title='Privacy Policy')