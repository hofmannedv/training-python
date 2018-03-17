# -----------------------------------------------------------
# demonstrates how to output an enumerated list
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# idea is based on: Python Tips - enumerate
# http://book.pythontips.com/en/latest/enumerate.html
# -----------------------------------------------------------

# define list of places
places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

# start number
start = 1

# start outputting the list of places beginning with the start number
for number, place in enumerate(places, start):
	print("%i: %s" % (number, place))
