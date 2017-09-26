# -----------------------------------------------------------
# demonstrates how to work with commandline arguments
# using the argparse module (available from Python 3.2)
# adding a program description
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard modules
import argparse

# define the program description
text = 'This is a test program. It demonstrates how to use the argparse module with a program description.'

# initiate the parser with a description
parser = argparse.ArgumentParser(description = text)
parser.parse_args()
