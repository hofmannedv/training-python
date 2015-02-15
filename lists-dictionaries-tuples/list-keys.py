# -----------------------------------------------------------
# demonstrates how to extract the keys of a dictionary using keys()
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

# extract the keys of the dictionary
countries = capital.keys()
print(countries)
