# -----------------------------------------------------------
# demonstrates how to work with commandline arguments
# determine the program/script name
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard modules
import sys

# evaluate the first argument, only
program = sys.argv[0]
print ("we are called as %s" % (program))

