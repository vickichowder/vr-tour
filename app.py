from flask import Flask, render_template, json, session, redirect, url_for, escape, request
from datetime import datetime
from os import getenv
import os

global guides
guides = {}
#server = 'tourwithme.database.windows.net'
#user = 'tourwithme@tourwithme'
#password = 'vr-tour2016'
#database = 'dev'
#port = '1433'

#conn = pymssql.connect(server, user, password, database, port)
#cursor = conn.cursor()

app = Flask(__name__)
app.debug = True


@app.route("/")
def main():
    return render_template('destinations.html')

@app.route("/add_guide")
def add_guide():
    if 'REPLACE_WITH_CITY' in guides:
        guides['REPLACE_WITH_CITY'].append(request.form['peerjs'])
    else:
        guides['REPLACE_WITH_CITY'] = [request.form['peerjs']]
    return len(guides['REPLACE_WITH_CITY'])

@app.route("/tourist")
def tourist():
    if 'REPLACE_WITH_CITY' in guides:
        ret = guides['REPLACE_WITH_CITY'][0]
        del guides['REPLACE_WITH_CITY'][0]
        return ret + " number of tour guides online!"

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/destinations")
def destinations():
    return render_template('destinations.html')

@app.route("/city/<city>")
def city(c):
    return render_template('city.html', c)

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
    app.run(port=int(os.environ.get('PORT', 33507)))
