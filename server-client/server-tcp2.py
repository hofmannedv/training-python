# -----------------------------------------------------------
# demonstrates a TCP server with basic communication
# based on socketserver.TCPserver Python module/class
#o
# (C) 2015,2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# based on: documentation for Python 3.5
# https://docs.python.org/3.5/library/socketserver.html
# -----------------------------------------------------------

import socketserver
import sys
import re

class MyTCPHandler(socketserver.BaseRequestHandler):
	# set datasize
	datasize = 1024
	
	def handle(self):
		# self.request is the TCP socket connected to the client
		self.data = self.request.recv(self.datasize).strip()
		print("[server] {} wrote:".format(self.client_address[0]))
		print(self.data)
		
		# just send back the same data, but upper-cased
		self.request.sendall(self.data.upper())

# ---- main program ----

# use localhost
host = ""

# define port to listen on
port = 12345

# Create the server, binding to localhost on port
server = socketserver.TCPServer((host, port), MyTCPHandler)

# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
server.serve_forever()

print (("[server] terminated."))
