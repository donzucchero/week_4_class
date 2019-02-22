from flask import Flask 
from web.public import course

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, world!"

app.register_blueprint(course, url_prefix = "/api/v5/course")




