# -----------------------------------------------------------
# reads the given data file, and imports it as sqlite database
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# call the program this way:
# python demo-db1.py database.sqlite

# import required python standard modules
import sys,sqlite3

# count number of program parameters
numPara = len(sys.argv)
if numPara < 2:
	print ("invalid number of parameters: 1 required.")
	print ("call: python %s database.sqlite" % sys.argv[0])
	print ("Exiting.")
	sys.exit(2)

# read name of the database file
databaseName = sys.argv[1]
print ("reading database from", databaseName, "...")

# open sqlite file
dbConnector = sqlite3.connect(databaseName)
cursor = dbConnector.cursor()

# read data structure

# committing changes to the database file
dbConnector.commit()

# close sqlite file
dbConnector.close()
