# -----------------------------------------------------------
# demonstrates how to calculate the sum of all prime numbers
# less than any number the user inputs
#o
# works for Python 2.x, only
#
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# included modules
import sys

# subroutines

def isPrime(number):
	# return True if prime number

	# set default value
	state = True

	# all numbers below 2 are not prime numbers
	if number < 2:
		state = False
	elif number == 2:
		# 2 is a prime number
		state = True
	else:
		divisionList = range(2, number-1)
		for i in divisionList:
			# if we find a a zero remainder, the number is not prime
			if number % i == 0:
				state = False
				break

	# return state value
	return state

# main program

# user prompt        
print('\nEnter any integer to get all the prime numbers that exist below it')
choice = int(raw_input(':'))

# validate user input
if type(choice) != int:
	# error message: no number
	print ("\ngiven input is not a number: %s ." % choice)

	# return with error state 1
	print ("\nexiting.")
	sys.exit(1)

# calculate list of prime numbers

primeNumbersList = []
for i in range(1,choice + 1):
	if isPrime(i):
		primeNumbersList.append(i)

print ("the prime numbers for %i are: " % i + " " + str(primeNumbersList))

count = len(primeNumbersList)
total = sum(primeNumbersList)
print("\nThe average of all these prime numbers is: %f" % (float(total)/float(count)))
print("\nThe sum of all these prime numbers is: %i" % total)

sys.exit(0)

