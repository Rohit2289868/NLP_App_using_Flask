from flask import Flask, render_template, request, redirect, session
from database import Database
import api
# render_template -> it loads the html files
# request -> it is used to fetch the input from html file

app = Flask(__name__)
dbo = Database()

@app.route('/') # when we hit this url index function will automatically called
def index():
    return render_template('login.html')

@app.route('/register') # when we hit '/register' this url register function will automatically called
def register():
    return render_template('register.html')

@app.route('/perform_registeration', methods=['post'])
def perform_registeration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message='Registration Successful. Kindly login to proceed')
    else:
        return render_template('register.html', message='Email already exists')

@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.search(email, password)
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html', message="Incorrect email/password")

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')
    response = api.NER(text)

    return render_template('ner.html', response=response)


app.run(debug=True) # app.run() will give the website link,
# and if 'debug=True' then we don't need to run the file again and again after making some changes