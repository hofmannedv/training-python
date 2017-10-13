#! /bin/bash

# -----------------------------------------------------------
# calculates the execution time of Python scripts
# uses the Python timeit module
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

for filename in *.py; do
	echo "$filename:"
	cat $filename | python3 -m timeit
	echo " "
done
