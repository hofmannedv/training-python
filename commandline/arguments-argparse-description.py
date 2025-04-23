# -----------------------------------------------------------
# demonstrates how to work with commandline arguments
# using the argparse module (available from Python 3.2)
# adding a program description
#o
# (C) 2017-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# include standard modules
import argparse

# define the program description
text = 'This is a test program. It demonstrates how to use the argparse module with a program description.'

# initiate the parser with a description
parser = argparse.ArgumentParser(description = text)
parser.parse_args()
