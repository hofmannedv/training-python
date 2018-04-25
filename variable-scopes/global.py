# -----------------------------------------------------------
# demonstrates global variables
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def info():
	"use two global variables name and age"
	
	print("%s is %i years old." % (name, age))
	return 

# define name and age
name = "Dominic"
age = 42

info()

