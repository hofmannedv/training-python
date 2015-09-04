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

# define character count function
def charStat (text):

	# set default value
	stat = {}

	# go through the characters one by one
	for character in text:
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

# open file for reading
fileHandle = open(textfileName, "r")

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

# output sorted list as CSV data
for item in sortedItems:
	print ("%s,%i" % (item[0], item[1]))

