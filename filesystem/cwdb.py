# -----------------------------------------------------------
# returns the current working directory as a binary string
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required python standard modules
import os

# detect the current working directory
path = os.getcwdb()
print ("the current working directory is %s" % path)
