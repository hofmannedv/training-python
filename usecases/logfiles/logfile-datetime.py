# -----------------------------------------------------------
# filter lines from a log file using datetime objects
#
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# -----------------------------------------------------------

# import required python standard modules
import sys
import os
import re
from datetime import datetime, time, date

def readFileContent(fileName):
	# read content of the given file
	# open file for reading
	fileId = open(fileName, 'r')
	
	# read content
	fileContent = fileId.readlines()
	
	# close file
	fileId.close()
	
	# return content
	return fileContent

def findEntryByTimestamp(fileContent, timestamp):
	# return all entries that have the given timestamp (date)
	
	# define empty entry list
	entries = []

	# define timestamp pattern
	# format: year-month-day hour:minute:second
	timestampPattern = timestamp.strftime("%Y-%m-%d %H:%M:%S")
	pattern = re.compile(timestampPattern)

	# go through the file content line by line
	for line in fileContent:
		# if we find the pattern in the current line ...
		if re.findall(pattern, line):
			# ... add the line to the list of entries
			entries.append(line)

	# return the entry list
	return entries

# analyze log file
# read commandline parameters
if len(sys.argv) > 1:
	# assume that the first parameter is a file to read data from
	# if the file exists, use this file
	if os.path.isfile(sys.argv[1]):
		logfileName = sys.argv[1]
	else:
		print ("Cannot read from given file", logfileName)
		print ("Exiting.")
		sys.exit(1)
else:
	print ("Parameter #1 missing: log file to analyze")
	print ("Exiting.")
	sys.exit(1)

print (("analyzed log file: %s") % (logfileName))

# retrieve file content
fileContent = readFileContent(logfileName)
#print(fileContent)

# find entries by exact timestamp
# - date
currentDate = date(2016, 1, 10)
# -time
currentTime = time(10, 45, 15)
# - timestamp
timestamp = datetime.combine(currentDate, currentTime)

print (("entries with timestamp for %s:") % (timestamp.ctime()))
entries = findEntryByTimestamp(fileContent, timestamp)
for singleEntry in entries:
	print (singleEntry)
