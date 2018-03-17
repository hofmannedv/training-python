# -----------------------------------------------------------
# demonstrates how to write a list to a file
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list of places
places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

# open file and write them to disk one after the next
with open('listfile.txt', 'w') as filehandle:
    for listitem in places:
        filehandle.write('%s\n' % listitem)

