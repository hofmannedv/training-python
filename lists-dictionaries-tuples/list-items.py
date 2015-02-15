# -----------------------------------------------------------
# demonstrates how to extract the items of a dictionary using items()
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define an array (dictionary)
capital = {
	"France": "Paris",
	"Switzerland": "Bern",
	"Germany": "Berlin"
	}

# output dictionary content (key-value-pairs)
print (capital)

# extract the items of the dictionary
entries = capital.items()

# count the items
print("#items:", len(entries))
print(entries)
