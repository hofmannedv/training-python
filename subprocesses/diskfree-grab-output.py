# -----------------------------------------------------------
# demonstrates how to run an external command using the
# subprocess library and to grab the output
#
# requires Python 3.5
#
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard modules
import subprocess

# call the command
output = subprocess.run(["df", "-h", "/home"], stdout=subprocess.PIPE)

# read the return code and the output data
print ("return code: %i" % output.returncode)
print ("output data: %s" % output.stdout)
