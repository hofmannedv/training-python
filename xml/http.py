# -----------------------------------------------------------
# demonstrates how to retrieve an mp3 file from a web resource
#
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard module
import httplib

# initiate a http connection
conn = httplib.HTTPConnection("www.semmel.ch")

# set a get request
conn.request("GET", "/bri/Live_und_Krank/BRI-LuK-Ethnic_Aggression.mp3")

# retrieve response
r1 = conn.getresponse()

# output response status, reason, and data length
print (r1.status, r1.reason, r1.length)

# in case we succeed ...
if r1.status == 200:
	# retrieve data
	print ("Datei vorhanden. Beziehe Daten ...")

	# open a temporary file
	fileHandle = open("/tmp/x.mp3", "w")

	# write the data
	fileHandle.writelines(r1.read())

	# clse the file
	fileHandle.close()
else:
	# output error message
	print ("Download geht grad nicht")

# close the connection
conn.close()
