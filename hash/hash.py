# -----------------------------------------------------------
# demonstrates how to use hash functions
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import hashlib

# print guaranteed hash functions
methods = hashlib.algorithms_guaranteed
for entry in methods:
	print(entry)

# create a hash
message = b"example"
mObject = hashlib.md5()
mObject.update(message)
print("md5 hash:" + mObject.hexdigest())
