# -----------------------------------------------------------
# demonstrates how to read a list from a file using pickle
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# load additional module
import pickle

with open('listfile.data', 'rb') as filehandle:
	# read the data as binary data stream
	placesList = pickle.load(filehandle)

print(placesList)
