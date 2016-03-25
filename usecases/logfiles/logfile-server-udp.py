# -----------------------------------------------------------
# demonstrates a server with basic communication (UDP)
# answering questions/requests regarding entries for a specific
# date in a log file
#o
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required python standard modules
import socket
import sys
import re
import os
from datetime import datetime, time, date

def readFileContent(fileName):
	# read content of the given file
	# open file for reading
	fileId = open(fileName, 'r')
	
	# read content
	fileContent = fileId.readlines()
	
	# close file
	fileId.close()
	
	# return content
	return fileContent

def findEntryByTimestamp(fileContent, timestamp):
	# return all entries that have the given timestamp (date)
	
	# define empty entry list
	entries = []

	# define timestamp pattern
	# format: year-month-day hour:minute:second
	timestampPattern = timestamp.strftime("%Y-%m-%d %H:%M:%S")
	pattern = re.compile(timestampPattern)

	# go through the file content line by line
	for line in fileContent:
		# if we find the pattern in the current line ...
		if re.findall(pattern, line):
			# ... add the line to the list of entries
			entries.append(line)

	# return the entry list
	return entries

# ---- define commandline setup, and read the logfile ----

# read commandline parameters
if len(sys.argv) > 1:
	# assume that the first parameter is a file to read data from
	# if the file exists, use this file
	if os.path.isfile(sys.argv[1]):
		logfileName = sys.argv[1]
	else:
		print ("[server] Cannot read from given file", logfileName)
		print ("[server] Exiting.")
		sys.exit(1)
else:
	print ("[server] Parameter #1 missing: log file to analyze")
	print ("[server] Exiting.")
	sys.exit(1)

print (("[server] analyzed log file: %s") % (logfileName))

# retrieve file content
fileContent = readFileContent(logfileName)

# ---- define udp server setup ----

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
		# as a message we may have received a timestamp
		# check that
		
		timestampPattern = re.compile("\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}")
		matches = re.findall(timestampPattern, message)
		if matches:
			# we have received a timestamp
			currentTimestamp = datetime.strptime(matches[0], "%Y-%m-%d %H:%M:%S")

			# look for logfile entries with this timestamp
			entries = findEntryByTimestamp(fileContent, currentTimestamp)

			for item in entries:
				print ("[server] logfile entry: %s" % item)
		else:
			print ("[server] %s" % message)
