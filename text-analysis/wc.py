# -----------------------------------------------------------
# reads the text from the given file, and outputs its 
# statistics regarding characters, words, and lines
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# call the program this way:
# python wc.py inputfile.txt

# import required python standard modules
import sys
import os
import re

# analyze text file
# assumption: this python file
textfileName = sys.argv[0]

# read commandline parameters
if len(sys.argv) > 1:
	# assume that the first parameter is a plaintext file
	# if the file exists, use this file
	if os.path.isfile(sys.argv[1]):
		textfileName = sys.argv[1]

print (("analyzed file: %s") % (textfileName))

# read file content
fileId = open(textfileName, 'r')
fileContent = fileId.readlines()
fileId.close()

# determine number of characters, assume: 0
characters = 0

# determine number of words, assume: 0
words = 0

# determine number of different words, assume: 0
differentWords = 0
wordList = {}

# go through the content line by line
for singleLine in fileContent:
	# count the number of characters per line
	characters = characters + len(singleLine)
	
	# read the new words
	newWords = re.split("\W+", singleLine)
	# print (newWords)

	for singleWord in newWords:
		if singleWord in wordList:
			wordList[singleWord] = wordList[singleWord] + 1
		else:
			wordList[singleWord] = 1

	words = words + len(newWords)

# calculate the file stats
lines = len(fileContent)
differentWords = len(wordList)

print (("number of lines: %i") % (lines))
print (("number of words: %i") % (words))
print (("number of different words: %i") % (differentWords))
print (("number of chars: %i") % (characters))
print ("word stat: ", wordList)

