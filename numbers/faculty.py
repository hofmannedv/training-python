# -----------------------------------------------------------
# demonstrates a recursive way to calculate the faculty of a number
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def faculty_recursive (number):
	if number == 0:
		return 1
	else:
		return number * faculty_recursive (number -1)

def faculty (number):
	result = 1
	while number > 1:
		result = result * number
		number = number - 1
	return result

number = 5
result = faculty_recursive(number)
result2 = faculty(number)
print ("The faculty of %i is %i" % (number, result))
print ("The faculty of %i is %i" % (number, result2))
