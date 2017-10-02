# -----------------------------------------------------------
# demonstrates how to run an external command using the
# subprocess library
#
# requires Python 3.5
#
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard modules
import subprocess

subprocess.run(["df", "-h", "/home"])

