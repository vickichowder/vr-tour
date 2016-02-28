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
cursor = conn.cursor()

# try:
# 	cursor.executemany(
#     "INSERT INTO tourist VALUES ('name', 'phone', 'street_number', 'street_name', 'city', 'state', 'country', 'username', 'password')",
#     [('Bob The Tourist', '4160983878', '34', 'University Avenue', 'Sunnyvale', 'CA', 'US', 'bobby', 'bobby')])
# 	conn.commit()
# 	print('inserted into table')
# 	cursor.execute('select * from tourist;')
# except:
# 	print('did not insert')

app = Flask(__name__)
app.debug = True

@app.route("/")
def main():

	return render_template('destinationslocals.html')

	return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            log_the_user_in(request.form['username'])
            return ""
        else:
            return 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    #return render_template('login.html', error=error)

@app.route("/home")
def signUp():
	return render_template('home.html')

@app.route("/signup")
def signup():
	return ""
	#return render_template('signup.html')

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

<<<<<<< HEAD
@app.route("/destinationslocals")
def destinationslocals():
	return render_template('destinationslocals.html')

=======
>>>>>>> cc8a7935142c1958356b29dc00a7b897c5387995
if __name__ == "__main__":
	app.run(port=8000)
