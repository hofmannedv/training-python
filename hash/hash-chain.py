# -----------------------------------------------------------
# demonstrates how to use hash functions -- hash chain
#o
# (C) 2018 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import hashlib
#import bitarray

def createHashChain(message, hashRange, algorithm):
	hashChain = []
	initialMessage = message.encode()
	if algorithm == "md5":
		mObject = hashlib.md5()
	elif algorithm == "sha1":
		mObject = hashlib.sha1()
	elif algorithm == "sha256":
		mObject = hashlib.sha256()
	
	while True:
		mObject.update(initialMessage)
		hashValue = mObject.hexdigest()[0:hashRange]
		
		if hashValue in hashChain:
			#print("hash chain:", hashChain)
			print("stopped at %s (entry at position %i)" % (hashValue, hashChain.index(hashValue)))
			break
		else:
			hashChain.append(hashValue)
			initialMessage = hashValue.encode()

	return hashChain

for length in [2,3,4]:
	for algorithm in ["md5", "sha1", "sha256"]:
		#hashChainList = []
		print("algorithm: %s, length: %s" % (algorithm, length))
		for i in range(15):
			message = str(i)
			hashChain = createHashChain(message, length, algorithm)
			print("start value %2i: %4i" % (i, len(hashChain)))
			print(hashChain)
			print("")

