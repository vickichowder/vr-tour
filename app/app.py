from flask import Flask, render_template, json, request, redirect
from datetime import datetime

app = Flask(__name__)
app.debug = True

# MySQL config
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ' '
app.config['MYSQL_DATABASE_DB'] = 'vr-tour'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

@app.route("/")
def main():
	return render_template('starttour.html')

@app.route("/login")
def login():
	return render_template('login.html')


@app.route("/signup")
def signUp():
	return render_template('signup.html')

@app.route("/destinations")
def destinations():
	return render_template('destinations.html')

@app.route("/requests")
def requests():
	return render_template('requests.html')

@app.route("/tourguidelist")
def tourguidelist():
	return render_template('tourguidelist.html')

@app.route("/starttour")
def starttour():
	return render_template('starttour.html')




if __name__ == "__main__":
	app.run(port=8000)
