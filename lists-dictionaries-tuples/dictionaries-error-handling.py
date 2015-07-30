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

# using the dict.get method
# Version 1 (with default value)
if capitals.get("Spain") == None:
	print("There is no entry for Spain")
else:
	city = capitals["Spain"]
	print("The capital of Spain is %s" % city)

# Version 2 (with alternative value)
city = capitals.get("Spain", "not in list")
print("The capital of Spain is %s" % city)

