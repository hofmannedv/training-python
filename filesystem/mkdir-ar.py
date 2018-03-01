# -----------------------------------------------------------
# creates a directory with specific access rights
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import the required python module
import os

# define the name of the directory to be created
path = "/tmp/year"

# define access rights
accessRights = 0o755

try:
	os.mkdir(path, accessRights)
except OSError:
	print ("creation of the directory %s failed" % path)
else:
	print ("successfully created the directory %s" % path)
