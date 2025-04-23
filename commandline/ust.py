#!/usr/bin/python

# -----------------------------------------------------------
# demonstrates how to work with commandline arguments using
# docopt (http://docopt.org/)
#
# example calculator for sales tax
#o
# (C) 2017-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

"""Usage:
    ./ust.py <value>
    ./ust.py -t <percentage> <value>
    ./ust.py --tax=percentage <value>
   
   Options:
    -t <percentage> <value> --tax=<percentage> <value>  calculate tax [default: 19]
"""

# include docopt module
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print (arguments)
    
    value = int(arguments["<value>"])
    percentage = int(arguments["--tax"])
    tax = value * percentage / 100
    print("the %i percent tax for %i is %.2f" % (percentage, value,tax))
