import os

import flask
import pyrebase
from flask import render_template
from flask import request, redirect

app = flask.Flask(__name__)
app.config.from_pyfile('./setting.py')

# firebase config
config = {
    "apiKey": app.config.get('FIREBASE_API_KEY'),
    "authDomain": app.config.get('FIREBASE_AUTH_DOMAIN'),
    "databaseURL": app.config.get('FIREBASE_DATABASE_URL'),
    "storageBucket": app.config.get('FIREBASE_STORAGE_BUCKET'),
    "serviceAccount": app.config.get('FIREBASE_CREDENTIAL')
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def create_app():
    app = Flask(__name__)
    return app

@app.route('/')
def index():
    data = db.child('post').get()
    return render_template('index.html', data = data)

@app.route('/create-post', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create-post.html')
    elif request.method == 'POST':
        data = dict(request.form)
        db.child("post").push(data)
        return redirect('/')

@app.route('/delete-post')
def destroy():
    id = request.args.get('data')
    db.child('post').child(id).remove()
    return redirect('/')