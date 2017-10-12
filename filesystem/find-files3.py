# -----------------------------------------------------------
# lists the files in the current directory using a subprocess
#
# works with Python 2 + 3
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required python standard modules
import subprocess

# define the ls command
ls = subprocess.Popen(["ls", "-p", "."], 
                      stdout=subprocess.PIPE,
                     )

# define the grep command
grep = subprocess.Popen(["grep", "-v", "/$"],
                     stdin=ls.stdout,
                     stdout=subprocess.PIPE,
                     )

# read from the end of the pipe (stdout)
endOfPipe = grep.stdout

# output the files line by line
for line in endOfPipe:
	print (line)
