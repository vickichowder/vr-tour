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
	return 'Vr-tour | Hacktech 2016'

#
# @app.route("/weAte", methods=['GET'])
# def weAte():
# 	# fetching from form
# 	guests = request.form['names']
# 	donation = request.form['amount']
# 	if (guests!="") and (donation!=""):
# 		return render_template('index.html')
# 	else:
# 		return render_template('index.html')

if __name__ == "__main__":
	app.run(port=8000)
