# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# demonstrates how to use the zip function
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define variables zipCode, place
zipCode = ["10247", "01015", "80123", "14467"]
place = ["Berlin", "Dresden", "München", "Potsdam"]

# combine both zipCode and place
address = zip(zipCode, place)

# output address
for item in address:
	print ("ZIP code: %s" % item[0])
	print ("place   : %s" % item[1])
	print (" ")
