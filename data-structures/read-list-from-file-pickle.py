# -----------------------------------------------------------
# demonstrates how to read a list from a file using pickle
#o
# (C) 2018-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# load additional module
import pickle

with open('listfile.data', 'rb') as filehandle:
	# read the data as binary data stream
	placesList = pickle.load(filehandle)

print(placesList)
