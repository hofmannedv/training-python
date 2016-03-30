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

try:
	# request data for an www service listening
	infolist = socket.getaddrinfo(
	hostname, 'www', 0, socket.SOCK_STREAM, 0,
	socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME
	)
except socket.gaierror, errorState:
	# no address associated with this hostname
	print ('Name service failure: %s' % (errorState.args[1]))
	sys.exit(1)

# output the retrieved information
# try the first one as recommended per standard
info = infolist[0]

# retrieve the socket arguments
socketArguments = info[0:3]

# retrieve the ip address
address = info[4]

# try to connect to the retrieved ip address
s = socket.socket(*socketArguments)
try:
	s.connect(address)
except socket.error, errorState:
	print ('Network failure: %s' % errorState.args[1])
else:
	print ('Success. The host %s is listening on port 80' % info[3])
