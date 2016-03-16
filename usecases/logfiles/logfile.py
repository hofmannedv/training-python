# -----------------------------------------------------------
# filter lines from a log file using regular expressions
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

def countLines(fileContent):
	# count the number of lines in the file
	return len(fileContent)

def getPart(fileContent, fromLine, toLine):
	# extract a certain part specified by line numbers
	
	# verify content range
	# adjust lower bound
	if fromLine < 0:
		fromLine = 0

	# adjust upper bound
	if toLine > countLines(fileContent):
		toLine = countLines(fileContent)

	# return content part
	return fileContent[fromLine:toLine]

def findEntryByUser(fileContent, username):
	# return all entries that contain a reference to the given username
	
	# define pattern
	pattern = re.compile(username)
	
	# define empty entry list
	entries = []

	# go through the file content line by line
	for line in fileContent:
		# if we find the pattern in the current line ...
		if re.findall(pattern, line):
			# ... add the line to the list of entries
			entries.append(line)

	# return the entry list
	return entries

def findEntryByLogin(fileContent, username):
	# return all the entries that contain a login entry for the given user
	
	# get all the entries that contain a reference to the given username
	userEntries = findEntryByUser(fileContent, username)

	# define empty entry list
	entries = []

	# define login pattern
	pattern = re.compile('logged in')

	# go through the user entries line by line
	for line in userEntries:
		# if we find the pattern in the current line ...
		if re.findall(pattern, line):
			# ... add the line to the list of entries
			entries.append(line)

	# return the entry list
	return entries

def findEntryByIPAddress(fileContent):
	# return all the entries that contain an ip address
	
	# define a very simple ip address pattern
	pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

	# define empty entry list
	entries = []

	# go through the file content line by line
	for line in fileContent:
		# if we find the pattern in the current line ...
		if re.search(pattern, line):
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

# find all entries for user fho
username = 'fho logged in'
print ("entries for user %s:" % (username))
entries = findEntryByUser(fileContent, username)
for singleEntry in entries:
	print (singleEntry)

# find all login entries for user james 
username = 'james'
print ("login entries for user %s:" % (username))
entries = findEntryByLogin(fileContent, username)
for singleEntry in entries:
	print (singleEntry)

# find entries by ip address
print ("entries with an ip address:")
entries = findEntryByIPAddress(fileContent)
for singleEntry in entries:
	print (singleEntry)
