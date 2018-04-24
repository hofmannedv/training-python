# -----------------------------------------------------------
# demonstrates local and global variables
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def calculateTax15 (value):
	"calculate the sales tax of 15% for the given value"
	
	# define sales tax as a local variable
	salesTax = 0.15
	
	# calculate the value plus tax
	total = value * salesTax
	return total

def calculateTax7 (value):
	"calculate the lower sales tax of 7% for the given value"
	
	# include salesTax into the local variable name space
	global salesTax
	
	# calculate the value plus tax
	total = value * salesTax
	return total

# define salesTax as a local variable to the main program
salesTax = 0.07

print ("15 percent tax of 100 is %.2f" % calculateTax15(100.0))
print ("7 percent of 100 is %.2f" % calculateTax7(100.0))

