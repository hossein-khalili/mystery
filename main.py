from flask import Flask, redirect, request
from flask import render_template
from flask import g
from database import db_session
from database import init_db
from models import User
import sys



app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/clocks', methods=['POST','GET'])
def level1():
	u = User.query.filter(User.name == 'farima').first()
	if(u.level >= 1):
		if request.method == 'GET':
			return render_template("level1.html")	
		elif request.method == 'POST':
			answer = request.form['answer']
			if answer.lower() == "live":
				u.level = 2
				db_session.add(u)
				db_session.commit()
				return redirect('/room')
			else :
				return "wrong!"
	else:
		return redirect("/")

@app.route('/room', methods=['POST','GET'])
def level2():
	u = User.query.filter(User.name == 'farima').first()
	if(u.level >= 2):
		if request.method == 'GET':
			return render_template("level2.html")
		elif request.method == 'POST':
			answer = request.form['answer']
			if answer.lower() == "this":
				u.level = 3
				db_session.add(u)
				db_session.commit()
				return redirect('/killer')
			else :
				return "wrong!"
	else:
		return redirect("/")

@app.route('/killer', methods=['POST','GET'])
def level3():
	u = User.query.filter(User.name == 'farima').first()
	if(u.level >= 3):
		if request.method == 'GET':
			return render_template("level3.html")	
		elif request.method == 'POST':
			answer = request.form['answer']
			if answer.lower() == "arsenic":
				u.level = 4
				db_session.add(u)
				db_session.commit()
				return redirect('/nameit')
			else :
				return "wrong!"
	else:
		return redirect("/")

@app.route('/nameit', methods=['POST','GET'])
def level4():
	u = User.query.filter(User.name == 'farima').first()
	if(u.level >= 4):
		if request.method == 'GET':
			return render_template("level4.html")	
		elif request.method == 'POST':
			answer = request.form['answer']
			if answer.lower() == "sandy":
				u.level = 5
				db_session.add(u)
				db_session.commit()
				return redirect('/catchme')
			else :
				return "wrong!"
	else:
		return redirect("/")

@app.route('/catchme', methods=['POST','GET'])
def level5():
	u = User.query.filter(User.name == 'farima').first()
	if(u.level >= 5):
		if request.method == 'GET':
			return render_template("final.html")
	else:
		return redirect("/")	



if __name__ == '__main__' :
	command = sys.argv[1]
	if command == "run":
		app.run(debug=True)
	if command == "check":
		print(User.query.all())
	if command == "init":
		init_db()
		u = User.query.filter(User.name == "farima").first()
		if u == None:
			u = User("farima", 1)
			db_session.add(u)
			db_session.commit()
		else:
			u.level = 1
			db_session.add(u)
			db_session.commit()
	

