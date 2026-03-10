# -----------------------------------------------------------
# demonstrates how to use the map function with an array
#
# (C) 2015-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define a simple function 
def addColumn(operand1, operand2, operand3):
    return operand1 + operand2 + operand3

# define a list of operands
operandList1 = [2.0, 4.0, 2.5]
operandList2 = [1.0, 2.0, 3.5]
operandList3 = [7.5, 0.5, 1.5]

# calculate the sum per column
sumPerColumn = map(addColumn, operandList1, operandList2, operandList3)

# output sums
for singleSum in sumPerColumn:
    print(singleSum)
