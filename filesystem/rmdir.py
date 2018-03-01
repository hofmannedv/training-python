# -----------------------------------------------------------
# deletes a directory
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import the required python module
import os

# define the name of the directory to be deleted
path = "/tmp/year"

try:
	os.rmdir(path)
except OSError:
	print ("deletion of the directory %s failed" % path)
else:
	print ("successfully deleted the directory %s" % path)
