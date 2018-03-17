# -----------------------------------------------------------
# demonstrates how to write a list to a file using writelines
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list of places
placesList = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

# open file and write them to disk one after the next
with open('listfile.txt', 'w') as filehandle:
	filehandle.writelines("%s\n" % place for place in placesList)

