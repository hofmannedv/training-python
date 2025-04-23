# -----------------------------------------------------------
# demonstrates how to work with commandline arguments
#o
# (C) 2014-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# include standard modules
import sys

# initiate a basic counter variable
count = 0

# count number of parameters
numPara = len(sys.argv) - 1
program = sys.argv[0]
print (("called %s with %i further parameters") % (program, numPara))

# output every argument we were called with
for parameter in sys.argv:
	print (count, ":", parameter)
	count = count + 1 
