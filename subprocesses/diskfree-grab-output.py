# -----------------------------------------------------------
# demonstrates how to run an external command using the
# subprocess library and to grab the output
#
# requires Python 3.5
#
# (C) 2017-2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# include standard modules
import subprocess

# call the command
output = subprocess.run(["df", "-h", "/home"], stdout=subprocess.PIPE)

# read the return code and the output data
print ("return code: %i" % output.returncode)
print ("output data: %s" % output.stdout)
