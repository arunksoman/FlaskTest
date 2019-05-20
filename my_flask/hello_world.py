from flask import Flask, render_template, request
import mysql.connector

from flask_wtf import Form
from wtforms import TextField

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_flaskTest"
)

cursor = db.cursor()

app = Flask(__name__)


@app.route('/')
def hello_world(title="Flask Server"):
	a = 3
	title = "Flask"
	return render_template('default.html', title=title,a = a)


@app.route('/login', methods = ['GET', 'POST'])
def login():

	return render_template('login-page.html')


if __name__ == '__main__':
   app.run(debug = True)