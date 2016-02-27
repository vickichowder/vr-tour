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
	return render_template('home.html')

@app.route("/login")
def comingUp():
	return render_template('login.html')

if __name__ == "__main__":
	app.run(port=8000)
