# -----------------------------------------------------------
# reads the text from the given file, and outputs its 
# character statistics 
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# call the program this way:
# python character-statistics.py inputfile.txt > statistics.csv

# import required python standard modules
import sys,csv
import codecs
import os

# define character count function
def charStat (text):

	# set default value
	stat = {}

	# go through the characters one by one
	for character in text:
		#print (character)
		# retrieve current value for a character, 
		# and 0 if still not in list
		# update the list
		stat[character] = stat.get(character,0) + 1

	# return statistics array
	return stat

# count number of program parameters
numPara = len(sys.argv)
if numPara < 2:
	print ("invalid number of parameters: 1 filename required.")
	print ("call for output on-screen: python %s " % sys.argv[0])
	print ("call for file output: python %s > statistics.csv" % sys.argv[0])
	print ("Exiting.")
	sys.exit(2)

# read name of the datafile
textfileName = sys.argv[1]
# print ("reading text from", textfileName, "...")

bytes = min(32, os.path.getsize(textfileName))
raw = open(textfileName, 'rb').read(bytes)

if raw.startswith(codecs.BOM_UTF8):
    encoding = 'utf-8-sig'
else:
    result = chardet.detect(raw)
    encoding = result['encoding']

# open file for reading
fileHandle = open(textfileName, "r", encoding=encoding)

# read content
data = fileHandle.read()

# close file
fileHandle.close()

# calculate the character statisitics
statistics = charStat(data)

# retrieve the single items 
items = statistics.items()

# print ("sorting by character ...")
# sort the items
sortedItems = sorted(items)

lines = []
# output sorted list as CSV data
for singleItem in sortedItems:
	lines.append(str(singleItem[0]) + "," + singleItem[1])
	#print ("%s,%i" % (singleItem[0], singleItem[1]))

# open file for writing
fileHandle = open("s.txt", "w", encoding=encoding)

# read content
data = fileHandle.writelines(lines)

# close file
fileHandle.close()


