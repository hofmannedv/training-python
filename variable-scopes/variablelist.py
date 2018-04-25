# -----------------------------------------------------------
# demonstrates the list of local and global variables
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def calculation():
	"do a complex calculation"
	
	global place
	place = "Cape Town"
	name = "John"
	
	print("place in global:", 'place' in globals())
	print("place in local :", 'place' in locals())
	print("name in global :", 'name' in globals())
	print("name in local  :", 'name' in locals())
	return

place = "Berlin"
print(place)
calculation()
print(place)
