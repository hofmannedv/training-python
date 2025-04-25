# -----------------------------------------------------------
# demonstrates how to write and call an inner function, or closure
#o
# (C) 2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

def increment (number):                        	# start of the outer function
    """increment by one"""
    def innerIncrement ():                  	# start of the inner function
        result = number + 1            		# process a new value
        return result                      	# return result of the calculation
    return innerIncrement()                    	# end of closure

def incrementTwo (number, value):              	# start of the outer function
    """increment by value"""
    def innerIncrement (value):                	# start of the inner function
        result = number + value        		# process a new value
        return result                      	# return result of the calculation
    return innerIncrement(value)               	# end of closure

# output result
print("the increment of 0 is", increment(0))	# call 1
print("the increment of 1 is", increment(1))	# call 2
print("the increment of 2 is", increment(2))	# call 3
print("the increment of 0 by 5 is", incrementTwo(0, 5))	# call 1
print("the increment of 1 by 10 is", incrementTwo(1, 10))	# call 2
print("the increment of 2 by 4 is", incrementTwo(2, 4))	# call 3
