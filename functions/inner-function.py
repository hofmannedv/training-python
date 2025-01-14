# -----------------------------------------------------------
# demonstrates how to write and call an inner function, or closure
#o
# (C) 2025 Frank Hofmann, Germany
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# email frank.hofmann@efho.de
# -----------------------------------------------------------

def increment (number):                        	# start of the outer function
    def innerIncrement ():                  	# start of the inner function
        result = number + 1            		# process a new value
        return result                      	# return result of the calculation
    return innerIncrement()                    	# end of closure

# output result
print("the increment of 0 is", increment(0))	# call 1
print("the increment of 1 is", increment(1))	# call 2
print("the increment of 2 is", increment(2))	# call 3
