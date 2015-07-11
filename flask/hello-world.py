# -----------------------------------------------------------
# basic flask application
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import flask module
from flask import Flask

# define flask application
application = Flask(__name__)

# define application path: bind function to specific url path
@application.route('/')
def helloWorld():
	# output welcome message
	return ("Hello, World!")

# main application start
if __name__ == "__main__":
	application.run()
