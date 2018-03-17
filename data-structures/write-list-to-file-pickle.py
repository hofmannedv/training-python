# -----------------------------------------------------------
# demonstrates how to write a list to a file using pickle
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# load additional module
import pickle

# define a list of places
placesList = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

with open('listfile.data', 'wb') as filehandle:
	# store the data as binary data stream
	pickle.dump(placesList, filehandle)

