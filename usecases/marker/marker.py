# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# set specific markers in a file if not set
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------
#

# include standard modules
import sys
import os.path

# count number of parameters
numPara = len(sys.argv)
if (numPara < 2):
	print ("called without further parameters. Exiting.")
	sys.exit(1)

# evaluate every argument we were called with
currentArg = 0
for parameter in sys.argv:
	if (currentArg > 0):
		#print ("file:", parameter)
		# does the given file exist?
		if not (os.path.isfile(parameter)):
			print ("file %s does not exist" % (parameter))
			print ("ignoring given parameter %s" % (parameter))
		else:
			# the file exists, so we can evaluate this file
			print ("evaluating file: %s" % (parameter))

			# open file for reading
			handle = open(parameter, "r")

			# read the whole file content
			content = handle.readlines()
			
			# close file
			handle.close()

			# evaluate the first five lines starting at line 0
			lines = 5
			linesOfContent = len(content)
			if (linesOfContent < 5):
				lines = linesOfContent

			# look for this comment: // filename
			# assume: not found
			alreadyWithComment = False

			currentLineId = 0
			while currentLineId < lines:
				if not alreadyWithComment:
					currentLine = content[currentLineId]
					print ("evaluating: %s" % (currentLine))

					# check the current line for the pattern
					if (currentLine.startswith("// " + parameter)):
						print ("comment found (file already marked properly)")
						alreadyWithComment = True

				# continue with the next line
				currentLineId = currentLineId + 1

			if not alreadyWithComment:
				# pattern not found -- so add comment to file content
				newContent = ["// " + parameter]
				for entry in content:
					newContent.append(entry)

				# open file for writing
				handle = open(parameter, "w")

				# output final file
				#print (newContent)
				for line in newContent:
					handle.write(line)

				# success message
				print ("comment added (file marked properly)")

				# close file
				handle.close()

	# continue with the next parameter
	currentArg += 1

# quit 
sys.exit(0)

