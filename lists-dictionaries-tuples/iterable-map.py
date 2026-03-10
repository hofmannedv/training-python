# -----------------------------------------------------------
# demonstrates how to use the map function
#
# (C) 2015-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define a simple function 
def powerValue(operand):
    return operand * operand

# define a list of operands
operandList1 = [2.0, 4.0, 2.5]
operandList2 = (1.0, 2.0, 433.5)

# output result
for currentList in (operandList1, operandList2):

    # start with first element at position #0
    currentPosition = 0

    # call powerValue for each item from operand list
    results = map(powerValue, currentList)

    # output results
    for i in results:
        # output a float value with 2 digits
        print("%8.2f:%10.2f" % (currentList[currentPosition],i))

        # increase current position
        currentPosition += 1
