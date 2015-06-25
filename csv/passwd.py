# -----------------------------------------------------------
# read /etc/passwd and extracts its content
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# use csv module
import csv

# define csv dialect using ":" as a field delimiter
csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)

# open file and extract fields
with open('/etc/passwd', 'r') as f:
	reader = csv.reader(f, 'unixpwd')
	for row in reader:
		print (row)
