# -----------------------------------------------------------
# flask microblog example application
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required modules
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# initialize the application and derive configuration
application = Flask(__name__)
application.config.from_object(__name__)

# load default configuration and override configuration from an
# environment variable
application.config.update(dict(
	DATABASE=os.path.join(application.root_path, 'flask-microblog.db'),
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))
application.config.from_envvar('FLASK_MICROBLOG_SETTINGS', silent=True)

# define subroutines
def connectDb():
	"connects to the specified database"
	database = application.config['DATABASE']
	databaseHandle = sqlite3.connect(database)

	databaseHandle.row_factory = sqlite3.Row
	return databaseHandle

def initDb():
	"initialize the sqlite database"
	with application.app_context():
		database = getDb()
		# read sql command from file
		with application.open_resource("schema.sql", mode="r") as f:
			# execute sql command
			database.cursor().executescript(f.read())
		# commit sql action
		database.commit()
	return

def getDb():
	"open a database connection if there is none yet for the current application context"
	if not hasattr(g, "sqlite_db"):
		g.sqlite_db = connectDb()

	return g.sqlite_db

@application.teardown_appcontext
def closeDb(error):
	"closes database connection"
	if hasattr(g, "sqlite_db"):
		g.sqlite_db.close()
	return

@application.route("/")
def showEntries():
	# display the blog entries
	database = getDb()
	
	# define sql command: all entries in descending order
	sqlCommand = "select title, text from entries order by id desc"
	
	# execute the sql command as defined above
	current = database.execute(sqlCommand)

	# fetch items from the database
	entries = current.fetchall()

	# return the rendered template
	return renderTemplate("show_entries.html", entries=entries)

@application.route("/add", methods=["POST"])
def addEntry():
	# add a blog entry
	
	# if not logged in quit with error
	if not session.get('logged_in'):
		abort(401)
	else:
		# get database connection
		database = getDb()

		# define sql command: add data from the microblog input fields
		sqlCommand = "insert into entries (title, text) values (?, ?)"

		# retrieve data
		insertData = [request.form["title"], request.form["text"]]

		# execute sql command
		database.execute(sqlCommand, insertData)

		# commit action
		database.commit()

		# add message
		flash("New entry was successfully posted")

		# return the rendered template / redirect url
		return redirect(url_for("show_entries"))

@application.route("/login", methods = ["GET", "POST"])
def login():
	# login procedure 
	
	# define error state: None
	error = None

	# check for POST requests
	if request.method == "POST":
		# check for the valid user name, and password
		if request.form["username"] != application.config["USERNAME"]:
			error = "Invalid user name"
		elif request.form["password"] != application.config["PASSWORD"]:
			error = "Invalid password"
		else: 
			# log in
			session["logged_in"] = True
			flash("You were logged in.")

			# return message: redirect to the entries page
			return redirect(url_for("show_entries"))

	# display login page with error message
	return render_template("login.html", error=error)

@application.route("/logout")
def logout():
	# logout procedure
	session.pop("logged_in", None)
	
	# place message
	flash("You were logged out")

	# return message: redirect to the entries page
	return redirect(url_for("show_entries"))

# run application
if __name__ == "__main__":
	# initialize the database
	initDb()

	# run the application
	application.run()
