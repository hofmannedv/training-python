# -----------------------------------------------------------
# demonstrates a server with basic communication
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import socket

# use localhost
host = ""

# define port to listen on
port = 12345

# define packet data size
dataSize = 1024

# init socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

requests = ["Hello", "3 + 4", "exit"]

# connect to server
s.connect((host,port))
print (("[client] connecting to server at %s:%i") % (host, port))

for data in requests:
	# send data
	print ("[client] sending data: %s" % data)
	s.send(data)

	# receive answer
	data = s.recv(dataSize)

	# output received data
	print ("[client] Received answer:", data)

# close connection
s.close()

