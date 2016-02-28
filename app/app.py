from flask import Flask, render_template, json, session, redirect, url_for, escape, request
from datetime import datetime
from os import getenv
import pymssql

server = 'tourwithme.database.windows.net'
user = 'tourwithme@tourwithme'
password = 'vr-tour2016'
database = 'dev'
port = '1433'

conn = pymssql.connect(server, user, password, database, port)
try:
    cursor = conn.cursor()
    print('connected to database')
except:
    print('did not connect to database')

try:
    cursor.execute(
    "INSERT INTO tourist VALUES ('name', 'phone', 'street_number', 'street_name', 'city', 'state', 'country', 'username', 'password')",
    [('Bob The Tourist', '4160983878', '34', 'University Avenue', 'Sunnyvale', 'CA', 'US', 'bobby', 'bobby')])
    conn.commit()
    print('inserted into table')
    print(cursor.execute('select * from tourist;').fetchone())
except Exception as e:
	print(e)
	print('did not insert')

app = Flask(__name__)
app.debug = True

@app.route("/")
def main():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		password = cursor.execute('select password from tourist where username=%s', request.form['username'])
		print(password.fetchone()[0])

		if request.form['password'] != password.fetchone()[0]:
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route("/home")
def signUp():
    return render_template('home.html')

@app.route("/signup")
def signup():
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


@app.route("/inprogress")
def inprogress():
    return render_template('inprogress.html')

@app.route("/endtour")
def endtour():
    return render_template('endtour.html')

@app.route("/billingpage")
def billingpage():
    return render_template('billingpage.html')

@app.route("/destinationslocals")
def destinationslocals():
	return render_template('destinationslocals.html')

if __name__ == "__main__":
    app.run(port=8000)
