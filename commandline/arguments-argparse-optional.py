# -----------------------------------------------------------
# demonstrates how to work with commandline arguments
# using the argparse module (available from Python 3.2)
# with an optional argument
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard modules
import argparse

# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("--version", "-V", help="show program version", action="store_true")
parser.parse_args()

# read arguments from the command line
args = parser.parse_args()

# check for --version
if args.version or args.V:
    print("this is myprogram version 0.1")
