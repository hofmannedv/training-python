# -----------------------------------------------------------
# read file content (iterator style)
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define the name of the file to read from
filename = "test.txt"

for line in open(filename, 'r'):
    print(line)

