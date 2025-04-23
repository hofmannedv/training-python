# -----------------------------------------------------------
# demonstrates how to work with commandline arguments
# determine the program/script name
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

# evaluate the first argument, only
program = sys.argv[0]
print ("we are called as %s" % (program))

