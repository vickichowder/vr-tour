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
    cursor.execute("""
        IF OBJECT_ID('persons', 'U') IS NOT NULL
        DROP TABLE persons
        CREATE TABLE persons (
        id INT ,
        name VARCHAR(100),
        salesrep VARCHAR(100),
        PRIMARY KEY(id)
        )
    """)
    cursor.execute("SELECT COUNT(id) FROM persons;")
    length = cursor.fetchone()[0]
    print(length+1)
    cursor.executemany(
        "INSERT INTO persons (id, name, salesrep) VALUES (%d, %s, %s)",
        [(length+1, 'John Smith', 'John Doe')])
    conn.commit()

    cursor.execute('SELECT * FROM persons')
    row = cursor.fetchone()
    while row:
        print("ID=%d, Name=%s" % (row[0], row[1]))
        row = cursor.fetchone()

    conn.close()
except Exception as e:
    print(e)
    print('did not insert')

app = Flask(__name__)
app.debug = True

def valid_login(username, password):
    cursor.execute("SELECT password FROM tourist where username=" + username)
    is_tourist = cursor.fetchone()[0]
    if is_tourist:
        if password == is_tourist:
            return True
        else:
            return False
    else:
        cursor.execute("SELECT password FROM host where username=" + username)
        is_host = cursor.fetchone()[0]
        if password == is_host:
            return True
        else:
            return False

@app.route("/")
def main():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return ""
        else:
            return 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    else:
        return render_template('login.html', error=error)


@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    error = None
    if request.method == 'POST':
        user_type = request.form['reg_person']
        cursor.execute("SELECT COUNT(id) FROM" + user_type +";")
        next = cursor.fetchone()[0]+1
        cursor.executemany(
            "INSERT INTO" + user_type + "(id, tourist_name, username, password, email) VALUES (%d, %s, %s, %s, %s, %s, %s)",
            [(next, request.form['reg_full_name'], request.form['reg_username'], request.form['reg_password'], request.form['full_email'])])
        conn.commit()

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

@app.route("/destinationslocals")
def destinationslocals():
    return render_template('destinationslocals.html')

if __name__ == "__main__":
    app.run(port=8000)
