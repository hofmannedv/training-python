# -----------------------------------------------------------
# demonstrates how to work with commandline arguments
# count the number of arguments
#o
# (C) 2017-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# include standard modules
import sys

# count the arguments
parameters = len(sys.argv) - 1
print ("we are called with %i parameters" % (parameters))

