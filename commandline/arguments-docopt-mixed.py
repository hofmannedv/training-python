#!/usr/bin/python

# -----------------------------------------------------------
# demonstrates how to work with commandline arguments using
# docopt (http://docopt.org/)
# short and long options
#o
# (C) 2017-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

"""Usage:
    ./arguments-docopt-mixed.py
    ./arguments-docopt-mixed.py [--help | -h]
    ./arguments-docopt-mixed.py [--verbose | -v]
   
   Options:
    --help -h     display help information
    --verbose -v  increase the verbosity of output
"""

# include docopt module
from docopt import docopt

if __name__ == '__main__':
	arguments = docopt(__doc__)
	print (arguments)
	
	if arguments["--verbose"]:
		print("enabling verbose output ")
