# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# create file differences
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------
#

import sys
import hashlib

def getHashValue(text):
	# calculate a hash fingerprint for the given text
	fingerprint = hashlib.sha256(text).hexdigest()
	return fingerprint

# evaluate command line options
commandLineOptions = sys.argv[1:]
if len(commandLineOptions) != 3:
	print ("""incorrect number of options:
distinct.py <input file> <pattern file> <output file>
Exiting.
""")
	sys.exit(1)

inputFile = commandLineOptions[0]
patternFile = commandLineOptions[1]
outputFile = commandLineOptions[2]

print ("input file: ", inputFile)
print ("pattern file: ", patternFile)
print ("output file: ", outputFile)

# prepare hash patterns
patternList = []

# read pattern file
patternContent = open(patternFile).readlines()
for line in patternContent:
	fingerprint = getHashValue(line)
	print ("%s: %s" % (line, fingerprint))
	if not fingerprint in patternList:
		patternList.append(fingerprint)

print ("%i patterns found" % len(patternList))

# open output file for writing
outputFileHandle = open(outputFile, "w")

# read input file
with open(inputFile, "r") as inputFileHandle:
	for line in inputFileHandle:
		fingerprint = getHashValue(line)
		if fingerprint not in patternList:
			print line
			outputFileHandle.write(line)

# close both input and output file
inputFileHandle.close()
outputFileHandle.close()
