# -----------------------------------------------------------
# creates a temporary directory 
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import the required python module
import tempfile

# create a temporary directory
with tempfile.TemporaryDirectory() as directory:
	print('the created temporary directory is %s' % directory)

# directory and contents have been removed
