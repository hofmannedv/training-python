# -----------------------------------------------------------
# demonstrates basic network address resolution
#
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# based on: A Simple TCP Client and Server described in the 
# book from Brandon Rhodes and John Goerzen: 
# Foundations of Python Network Programming
# apress, 2010, ISBN 978-1-4302-3003-8
# -----------------------------------------------------------

import socket

# retrieve local hostname
localHostname = socket.gethostname()

# get fully qualified hostname
localFqdn = socket.getfqdn()

print ("working on %s (%s)" % (localHostname, localFqdn))

# use example domain (CERN, Geneva)
hostname = 'cern.ch'
print ("checking for domain %s ..." % hostname)

# get the according IP address
ipAddress = socket.gethostbyname(hostname)
print ("The server for %s answers with the IP address %s" % (hostname, ipAddress))
