# -----------------------------------------------------------
# demonstrates how to use hash functions -- repeated hash
#o
# (C) 2018-2026 Frank Hofmann, Berlin/Freiburg, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
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

