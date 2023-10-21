# -----------------------------------------------------------
# demonstrates basic client-/server communication
#
# (C) 2018-2023 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# -----------------------------------------------------------

# load additional Python modules
import socket
import time

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
localHostname = socket.gethostname()

# get fully qualified hostname
localFqdn = socket.getfqdn()

# get the according IP address
ipAddress = socket.gethostbyname(localHostname)

# bind the socket to the port 23456, and connect
serverAddress = (ipAddress, 23456)
sock.connect(serverAddress)
print ("connecting to %s (%s) with %s" % (localHostname, localFqdn, ipAddress))

# define example data to be sent to the server
temperatureData = ["15", "22", "21", "26", "25", "19"]
for entry in temperatureData:
	print ("data: %s" % entry)
	newData = str("temperature: %s\n" % entry).encode("utf-8")
	sock.sendall(newData)
	
	# wait for two seconds
	time.sleep(2)

# close connection
sock.close()
