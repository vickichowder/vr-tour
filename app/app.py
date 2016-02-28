from flask import Flask, render_template, json, session, redirect, url_for, escape, request
from datetime import datetime
from os import getenv
import pymssql
#
# server = 'tourwithme.database.windows.net'
# user = 'tourwithme'
# password = 'vr-tour2016'
# database = 'dev'
#
# conn = pymssql.connect(server, user, password, database)
# cursor = conn.cursor()

app = Flask(__name__)
app.debug = True

@app.route("/")
def main():
	return render_template('starttour.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

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
