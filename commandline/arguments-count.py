# -----------------------------------------------------------
# demonstrates how to work with commandline arguments
# count the number of arguments
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard modules
import sys

# count the arguments
parameters = len(sys.argv) - 1
print ("we are called with %i parameters" % (parameters))

