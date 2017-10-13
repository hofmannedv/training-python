# -----------------------------------------------------------
# lists the files in the current directory using os.walk
# includes time measurement to get the execution time
#
# works with Python 2 + 3
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required python standard modules
import os, timeit

startTime = timeit.default_timer()

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)

elapsedTime = timeit.default_timer() - startTime
print(elapsedTime)
