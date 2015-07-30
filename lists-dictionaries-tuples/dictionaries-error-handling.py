# -----------------------------------------------------------
# demonstrates different ways of error handling
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a dictionary of capitals
capitals = {
	"Norway": "Oslo",
	"Germany": "Berlin",
	"France": "Paris"
}
print("original:", capitals)

# EAFP: Easier to Ask Forgiveness than Permission
try:
	city = capitals["Spain"]
	print("The capital of Spain is %s" % city)
except KeyError:
	print("There is no entry for Spain")

# LBYL: Look Before You Leap
# Version 1:
if "Spain" in capitals:
	city = capitals["Spain"]
	print("The capital of Spain is %s" % city)
else:
	print("There is no entry for Spain")

# Version 2:
if capitals.has_key("Spain"):
	city = capitals["Spain"]
	print("The capital of Spain is %s" % city)
else:
	print("There is no entry for Spain")

# dict.get method
