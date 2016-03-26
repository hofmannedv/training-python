# -----------------------------------------------------------
# demonstrates a TCP server with basic communication
#o
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
			raise EOFError('[server] socket closed %d bytes into a %d-byte message' % (len(data), length))

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

# set socket options
# - SOL_SOCKET:
# - SO_REUSEADDR: previous execution has left the socket in a TIME_WAIT state
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind host and port to the socket
s.bind((host,port))

# listen to exactly one connection
s.listen(1)

print (("[server] started at %s:%i") % (host, port))
print ("[server] waiting for requests ...")

while True:

	# listening
	print ('[server] Listening at', s.getsockname())

	# wait for connections, and accept
	client, address = s.accept()
	remoteIPAddress, remotePort = address
	print ('[server] accepted a connection from %s:%i' % (remoteIPAddress, remotePort))
	print ('[server] socket connects', client.getsockname(), 'and', client.getpeername())

	# retrieve 16 byte of data from the client
	data = receiveAllData(client, 16)
	print ('[server] message:', repr(data))

	# send reply to client
	client.sendall('Farewell, client')

	# close socket/connection
	client.close()
	print ('[server] reply sent, and socket is closed')

print (("[server] terminated."))
