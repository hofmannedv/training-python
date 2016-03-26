# -----------------------------------------------------------
# demonstrates a TCP client with basic communication
#
# (C) 2015,2016 Frank Hofmann, Berlin, Germany
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
import re

def receiveAllData(socketId, length):
	# receive all data for a request
	
	# received data is empty (default value)
	data = ''

	# read data as long as there is data to read
	while len(data) < length:
		# try to read as many data as possible
		more = socketId.recv(length - len(data))
		if not more:
			raise EOFError('[client] socket closed %d bytes into a %d-byte message' % (len(data), length))

		# combine the data we retrieved so far
		data += more
	
	# return the data we retrieved
	return data

# ---- main program ----

# use localhost
host = ""

# define port to listen on
port = 12345

# define packet data size
dataSize = 1024

# init stream socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
s.connect((host,port))
print (("[client] connecting to server at %s:%i") % (host, port))
print ("[client] assigned socket name:", s.getsockname())

# send data to server
s.sendall('Hi there, server')

# retrieve reply from server
reply = receiveAllData(s, 16)
print ('[client] the server replied: %s' % repr(reply))

# close connection
s.close()

