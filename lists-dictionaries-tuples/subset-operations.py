# -----------------------------------------------------------
# demonstrates how to work with subsets 
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define set of capitals
capitalsEurope = set(["Berlin", "Oslo", "Bern"])
capitalsAsia = set(["Tokio", "Delhi", "Hanoi"])
print("original:", capitalsEurope)
print("original:", capitalsAsia)

# unite two sets
capitalsEurasia = capitalsEurope | capitalsAsia
print("united set:", capitalsEurasia)

# calculate the elements that are part of both set 1, and 2
capitalsBoth = capitalsEurasia & capitalsAsia
print("both set:", capitalsBoth)

# calculate the difference set
capitalsDifference = capitalsEurasia - capitalsAsia
print("difference set:", capitalsDifference)

# test if a specific element is part of a set
if "Hanoi" in capitalsBoth:
	print("Hanoi is part of capitalsBoth")
