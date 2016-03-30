# -----------------------------------------------------------
# demonstrates identifying services by its port name
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

# define list of network protocols
portList = [22, 80, 443]

for port in portList:
	protocol = socket.getservbyport(port)

	# print port and protocol as well-formatted output
	print ('%4i: %s' % (port, protocol))

