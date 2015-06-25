# -----------------------------------------------------------
# demonstrates the detection of colour codes using regular 
# expressions
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import re

# define pattern
pattern = "[^a-f0-9]+"
prog = re.compile(pattern)

# define a list of colour codes
colourCodes = ["fff", "234000", "abx", "03g", "z3a"]

# detect the codes in a loop
for code in colourCodes:
	if re.match(prog, code):
		print ("%s is a valid colour code" % code)
