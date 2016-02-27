from flask import Flask, render_template, json, request, redirect
from datetime import datetime

app = Flask(__name__)

# MySQL config
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ' '
app.config['MYSQL_DATABASE_DB'] = 'vr-tour'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

@app.route("/")
def main():
	return render_template('reglogin.html')



if __name__ == "__main__":
	app.run(port=8000)
