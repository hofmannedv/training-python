# -----------------------------------------------------------
# lists the files in the current directory using pathlib
#
# works with Python 3
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required python standard modules
import pathlib

# define the path 
currentDirectory = pathlib.Path('.')

for currentFile in currentDirectory.iterdir():
    print(currentFile)
