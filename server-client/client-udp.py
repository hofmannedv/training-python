# -----------------------------------------------------------
# demonstrates a client with basic communication (UDP)
#o
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import socket

# use localhost
host = '127.0.0.1'

# define port to listen on
port = 12345

# define packet data size
dataSize = 1024

# init socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ("[client] address before sending:", s.getsockname())

# define requests
requests = ["Hello", "3 + 4", "10 * 5", "quit"]

for data in requests:
	# send data
	print ("[client] sending data: %s" % data)
	s.sendto(data, (host, port))
	
	print ("[client] address after sending:", s.getsockname())
