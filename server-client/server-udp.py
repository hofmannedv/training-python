# -----------------------------------------------------------
# demonstrates a server with basic communication (UDP)
#o
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import socket
import sys
import re

# use localhost
host = ""

# define port to listen on
port = 12345

# define maximum packet data size
dataSize = 1024

# init socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind host and port to the socket
s.bind((host,port))

# output server welcome message
print (("[server] started at %s:%i") % (host, port))
print (("[server] waiting for requests ..."))

while True:
	# receive data from the client
	data, address = s.recvfrom(dataSize)
	
	# decode the binary message from the client
	message = data.decode(encoding="utf-8", errors="strict")
	
	# output the received message
	print ("[server] The client at", address, "says", message)
	
	# evaluate the message
	if (message == "quit"):
		# the server is asked to terminate
		print ("[server] terminated.")
		sys.exit(0)
	else:
		# define a specific calculation pattern: 
		# number, spaces, operator, spaces, number
		calculationPattern = re.compile("\d+\s+[:\+\-\*]\s+\d+")
		if re.match(calculationPattern, message):
			# we received a calculation request
			print ("[server]: ", message, "evaluates to", eval(message))
		else:
			# we received sth else
			print ("[server]:", message)
