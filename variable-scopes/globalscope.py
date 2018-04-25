# -----------------------------------------------------------
# demonstrates how to modify global variables (reading and 
# writing)
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def location():
	"redefine the current location"
	
	global place
	place = "Cape Town"
	
	return

place = "Berlin"
print(place)
location()
print(place)
