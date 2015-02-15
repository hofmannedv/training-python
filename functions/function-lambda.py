# -----------------------------------------------------------
# demonstrates how to write and call a lambda function
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define lambda functions (short functions without loops, output etc.)
multiplication = lambda x,y: x*y
addition = lambda x,y: x+y

# main program
product = multiplication(4,5)
sum = addition(3,8)

print("product:", product)
print("sum:", sum)
