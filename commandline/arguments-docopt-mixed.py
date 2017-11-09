#!/usr/bin/python

# -----------------------------------------------------------
# demonstrates how to work with commandline arguments using
# docopt (http://docopt.org/)
# short and long options
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

"""Usage:
    ./arguments-docopt-mixed.py
    ./arguments-docopt-mixed.py [--help | -h]
    ./arguments-docopt-mixed.py [--version | -v]
   
   Options:
    --help -h     display help information
    --version -v  increase the verbosity of output
"""

# include docopt module
from docopt import docopt

if __name__ == '__main__':
	arguments = docopt(__doc__)
	print (arguments)
	
	if arguments["--version"]:
		print("enabling verbose output ")
