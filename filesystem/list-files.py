# -----------------------------------------------------------
# lists the files in the current directory 
# based on the Python 3.6 documentation
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required python standard modules
import os

# detect the current working directory
path = os.getcwd()

# read the entries
with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        # print all entries that are files
        if entry.is_file():
            print(entry.name)
