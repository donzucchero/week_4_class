from flask import Blueprint, render_template


course = Blueprint('user', __name__, template_folder='templates')
 
courses_list = ["John", "Jack"]

@course.route('/')
def course_list():
    return render_template('index.html', courses = courses_list)