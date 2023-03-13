from flask import Flask, render_template, request,redirect, session
from db import Database
import api

app = Flask(__name__)
dbo = Database()

@app.route('/')  # whenever someone puts a slash in front of the website following functions will be triggered.
def index():
    return render_template('Login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration', methods=["post"])
def perform_registration():
    name = request.form.get('Users_Name')
    email = request.form.get('Users_Email')
    password = request.form.get('Users_Password')
    response = dbo.insert(name,email,password)

    if response:
        return render_template('Login.html',message='Registration Successful. Kindly Login to proceed')
    else:
        return render_template('register.html', message='Email already exists')

@app.route('/perform_login', methods=["post"])
def perform_login():
    email = request.form.get('Users_Email')
    password = request.form.get('Users_Password')

    response = dbo.search(email,password)

    if response:
        return redirect('/profile')
    else:
        return render_template('Login.html',message = 'Incorrect email/password')

@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text=request.form.get('ner_text')
    response=api.ner(text)
    print(response)
    return render_template('ner.html',response=response)

@app.route('/emotion')
def emotion():
    return render_template('emotion.html')

@app.route('/perform_emotion', methods=['post'])
def perform_emotion():
    text = request.form.get('emotion_text')
    response = api.emotion(text)
    print(response)
    return render_template('emotion.html',response = response)



app.run(debug=True)
