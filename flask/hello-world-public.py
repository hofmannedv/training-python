# -----------------------------------------------------------
# basic flask application with public access, and in debug mode
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
	return ("Hello, World! Nice to see you!")

# main application start
# - available/access from everywhere (set host to "0.0.0.0")
# - debug mode enabled (set debug to True)
# - reloading the server automatically if python code changes
if __name__ == "__main__":
	application.run(host="0.0.0.0", debug=True)

	# alternatively, enable the application debug flag like this:
	# application.debug = True

