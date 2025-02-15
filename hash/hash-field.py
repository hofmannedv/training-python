# -----------------------------------------------------------
# demonstrates how to use hash functions -- repeated hash
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import hashlib

# create a hash
mObject = hashlib.md5()
initialMessage = "example".encode()[0:4]

iteration = 1
while iteration < 25:
	mObject.update(initialMessage)
	md5hash = mObject.hexdigest()
	print("md5 hash for ", initialMessage, " on level ", iteration, ": ", md5hash)
	iteration += 1
	initialMessage = md5hash.encode()[0:4]

