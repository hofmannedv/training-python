# -----------------------------------------------------------
# demonstrates how to write and call a lambda function
#o
# (C) 2015-2025 Frank Hofmann, Berlin/Freiburg, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define lambda functions (short functions without loops, output etc.)
multiplication = lambda x,y: x*y
addition = lambda x,y: x+y

# main program
product = multiplication(4,5)
sum = addition(3,8)

# output the result of the function calls
print("product:", product)
print("sum:", sum)
