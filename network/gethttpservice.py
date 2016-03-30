# -----------------------------------------------------------
# demonstrates a web server test
#
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# based on: A Simple TCP Client and Server described in the 
# book from Brandon Rhodes and John Goerzen: 
# Foundations of Python Network Programming
# apress, 2010, ISBN 978-1-4302-3003-8
# -----------------------------------------------------------

import socket
import sys

# check commandline arguments
if len(sys.argv) != 2:
	print ("usage: gethttpservice.py hostname|ip-address")
	sys.exit(2)

# derive hostname from the commandline arguments
hostname = sys.argv[1]
print ("checking for domain %s ..." % hostname)

