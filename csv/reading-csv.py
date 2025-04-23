# -----------------------------------------------------------
# reads the given data file, and imports it as csv file
#o
# (C) 2014-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# call the program this way:
# python reading-csv.py database.txt

# import required python standard modules
import sys,csv

# count number of program parameters
numPara = len(sys.argv)
if numPara < 2:
	print ("invalid number of parameters: 1 required.")
	print ("call: python %s database.txt" % sys.argv[0])
	print ("Exiting.")
	sys.exit(2)

# read name of the datafile
datafileName = sys.argv[1]
print ("reading database from", datafileName, "...")

lines = 0
with open(datafileName) as csvfile:
	reader = csv.DictReader(csvfile)

	# read the data from csv file, and output the data fields
	# the  first line contains the names of the columns that are used as keys

	for row in reader:
		# read columns
		nameEntry, addressEntry, cityEntry, zipEntry, countryEntry = row["Name"], row["Address"], row["City"], row["Zip"], row["Country"]

		print (("Name and place: %s,%s") % (nameEntry, cityEntry))

		# increase the line counter
		lines += 1

# output the number of lines read from database
print ("... read", lines, "lines")


