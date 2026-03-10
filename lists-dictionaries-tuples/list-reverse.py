# -----------------------------------------------------------
# demonstrates how to reverse a list
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a list
basicList = [3, 47, 12, 15]
print("original order:", basicList)

print("reversed order using the index:", basicList[::-1])

print("reversed order using reversed function:", list(reversed(basicList)))
