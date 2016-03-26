# -----------------------------------------------------------
# demonstrates a server with basic communication
#o
# (C) 2015,2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# based on: A Simple TCP Client and Server described in the book
# Brandon Rhodes and John Goerzen: Foundations of Python Network
# Programming, apress, ISBN 978-1-4302-3003-8
# -----------------------------------------------------------

import socket
import sys
import re

def receiveAllData(socketId, length):
	# receive all data for a request
	# received data is empty
	data = ''
	while len(data) < length:
		

# use localhost
host = ""

# define port to listen on
port = 12345

# define packet data size
dataSize = 1024

# init stream socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind host and port to the socket, set connection limit
s.bind((host,port))
s.listen(maxConnections)

print (("[server] started at %s:%i") % (host, port))
print (("[server] waiting for requests ..."))

terminate = False

while terminate == False:
	# wait for connections, and accept
	client, address = s.accept()

	# receive data coming in
	data = client.recv(dataSize)

	# process data
	if data:
		print ("[server] accepted request: %s" % data)

		# check for termination request
		if data in ["quit", "exit", "halt"]:
			print ("[server] received termination request")
			# return result
			client.send("0")
			terminate = True

		elif data in ["Hello"]:
			client.send("Hello, client :)")

		else:
			# evaluate command
			result = eval(data)
			# return result of the evaluation
			client.send(result)

	# close connection
	client.close() 
	print ("[server] closing connection")

	if terminate == True:
		break

print (("[server] terminated."))
