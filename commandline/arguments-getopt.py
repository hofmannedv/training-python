# -----------------------------------------------------------
# demonstrates how to work with commandline arguments using getopt
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard modules
import getopt, sys

# read commandline arguments, first
fullCmdArguments = sys.argv

print (fullCmdArguments)

# - program name
program = fullCmdArguments[0]

# - further arguments
argumentList = fullCmdArguments[1:]

# define possible unix options
unixOptions = "ho:v"
gnuOptions = ["help", "output=", "verbose"]

try:
	options, arguments = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
	# output error, and return with an error code
	print (str(err))
	sys.exit(2)

# evaluate given options
for currentOption, currentArgument in options:
	if currentOption in ("-v", "--verbose"):
		print ("enabling verbose mode")
	elif currentOption in ("-h", "--help"):
		print ("displaying help")
	elif currentOption in ("-o", "--output"):
		print (("enabling special output mode (%s)") % (currentArgument))
