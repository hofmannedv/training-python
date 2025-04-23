# -----------------------------------------------------------
# demonstrates how to work with commandline arguments
# using the argparse module (available from Python 3.2)
# with an optional argument
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

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--version", "-V", help="show program version", action="store_true")

# read arguments from the command line
args = parser.parse_args()

# check for --version
if args.version:
    print("this is myprogram version 0.1")
