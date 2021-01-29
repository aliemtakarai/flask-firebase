import os

import flask
from flask import render_template

app = flask.Flask(__name__)

def create_app():
    app = Flask(__name__)
    return app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-post')
def create():
    return render_template('create-post.html')