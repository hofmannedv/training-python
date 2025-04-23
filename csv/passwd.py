# -----------------------------------------------------------
# read /etc/passwd and extracts its content
#o
# (C) 2015-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
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
