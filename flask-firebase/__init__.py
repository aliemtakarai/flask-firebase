import os

import flask
import pyrebase
from flask import render_template

app = flask.Flask(__name__)

# firebase config
config = {
    "databaseURL": app.config.get('firebase_database_url'),
    "serviceAccount": app.config.get('firebase_credential')
}

firebase = pyrebase.initialize_app(config)

def create_app():
    app = Flask(__name__)
    return app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-post')
def create():
    return render_template('create-post.html')