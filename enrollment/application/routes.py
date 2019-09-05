from application import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home_page():
	return render_template("index.html", login=False)

@app.route('/register')
def register_page():
	return render_template("register.html", login=False)

@app.route('/login')
def login_page():
	return render_template("login.html", login=False)

@app.route('/courses')
def courses_page():
	return render_template("courses.html", login=False)