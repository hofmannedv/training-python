# -----------------------------------------------------------
# reads the given data file, and imports it as sqlite database
# simply outputs the names of the tables found in the database
#o
# (C) 2015-2026 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# call the program this way:
# python demo-db1.py database.sqlite

# import required python standard modules
import sys, sqlite3, os

# count number of program parameters
numPara = len(sys.argv)
if numPara < 2:
    print ("invalid number of parameters: 1 required.")
    print (f"call: python {sys.argv[0]} database.sqlite")
    print ("exiting with error code 2.")
    sys.exit(2)

# read name of the database file
databaseName = sys.argv[1]
print (f"trying to read database from {databaseName} ...")

# does the database file exist?
if not os.path.isfile(databaseName):
    print(f"cannot read database from {databaseName}")
    print ("exiting with error code 3.")
    sys.exit(3)

# open sqlite file
try:
    dbConnector = sqlite3.connect(databaseName)
    print(f"connection established at {dbConnector}")

    # create database cursor
    cursor = dbConnector.cursor()
    print(f"cursor established at {cursor}")

    # read data structure: tables in the database
    sqlInstruction = "SELECT name FROM sqlite_master"
    result = cursor.execute(sqlInstruction)
    print(f"found the following tables in the database: {result.fetchall()}")

    # close sqlite file
    print("closing database connection")
    dbConnector.close()
except:
    print(f"cannot open given database file: {databaseName}")
    print ("exiting with error code 1.")
    sys.exit(1)
