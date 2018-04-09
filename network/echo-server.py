# -----------------------------------------------------------
# demonstrates basic client-/server communication
#
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# -----------------------------------------------------------

# load additional Python module
import socket

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
localHostname = socket.gethostname()

# get fully qualified hostname
localFqdn = socket.getfqdn()

# get the according IP address
ipAddress = socket.gethostbyname(localHostname)

# output hostname, domain name and IP address
print ("working on %s (%s) with %s" % (localHostname, localFqdn, ipAddress))

# bind the socket to the port 23456
serverAddress = (ipAddress, 23456)
print ('starting up on %s port %s' % serverAddress)
sock.bind(serverAddress)

# listen for incoming connections (server mode) with one connection at a time
sock.listen(1)

while True:
    # wait for a connection
    print ('waiting for a connection')
    connection, clientAddress = sock.accept()

    try:
        # show who connected to us
        print ('connection from', clientAddress)

        # receive the data in small chunks and print it
        while True:
            data = connection.recv(64)
            if data:
                # output received data
                print ("Data: %s" % data)
            else:
                # no more data -- quit the loop
                print ("no more data.")
                break
    finally:
        # Clean up the connection
        connection.close()
