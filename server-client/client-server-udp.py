# -----------------------------------------------------------
# demonstrates an interaction between client and server (UDP)
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

# check for commandline options
if sys.argv[1:] == ['server']:
	# run as server
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
			# return an answer to the client
			s. sendto('Your data was %d bytes' % len(message), address)

elif sys.argv[1:] == ['client']:
	# run as client, instead

	print ("[client] address before sending:", s.getsockname())

	# define requests
	requests = ["Hello", "Good morning!", "How are you?", "quit"]

	for data in requests:
		# send data
		print ("[client] sending data: %s" % data)
		s.sendto(data, (host, port))
		print ("[client] address after sending:", s.getsockname())

		# received answer from server
		data, address = s.recvfrom(dataSize)
		print ('[client] The server at', address, 'says', repr(data))
	
	sys.exit(0)

else:
	print ("Parameter is missing: either server, or client")
	print ("Exiting.")
	sys.exit(1)
