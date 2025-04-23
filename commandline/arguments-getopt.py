# -----------------------------------------------------------
# demonstrates how to work with commandline arguments using getopt
#o
# (C) 2014-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
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
