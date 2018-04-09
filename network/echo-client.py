# -----------------------------------------------------------
# demonstrates basic client-/server communication
#
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
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
