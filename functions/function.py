# -----------------------------------------------------------
# demonstrates how to write and call a function, basically
#o
# (C) 2015-2026 Frank Hofmann, Berlin/Freiburg, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# a simple function without parameters
def functionOne():
    print("in functionOne.")

    # define a boolean value as a return value
    return True

# another function with a parameter
def functionTwo(parameter):
    print("in functionTwo")
    print("parameter has this value:", parameter)

    # define a single return value
    return 7

# another function with an optional parameter
def functionThree(parameter="default value"):
    print("in functionThree")
    print("parameter has this value:", parameter)

    # define a single return value
    return 7

# main program
# - calling functionOne without parameters
returnValue1 = functionOne()
print("return value:", returnValue1)
print()

# - calling functionTwo with a parameter 1
returnValue2 = functionTwo(1)
print("return value:", returnValue2)
print()

# - calling functionThree with a parameter 1
returnValue3 = functionThree(1)
print("return value:", returnValue3)
print()

# - calling functionThree without a parameter
returnValue4 = functionThree()
print("return value:", returnValue4)

