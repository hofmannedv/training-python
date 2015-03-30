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

# output every argument we were called with
currentArg = 0
for parameter in sys.argv:
	if (currentArg > 0):
		#print ("file:", parameter)
		if not (os.path.isfile(parameter)):
			print ("file %s does not exist" % (parameter))
			print ("ignoring file")
		else:
			print ("evaluating file:", parameter)
			# open file for reading
			handle = open(parameter, "r")

			# read the whole file content
			content = handle.readlines()
			
			# close file
			handle.close()

			# evaluate the first five lines starting at line 0
			linesOfContent = len(content)
			lines = 5
			if (linesOfContent < 5):
				lines = linesOfContent

			# look for this comment: // filename
			# assume: not found
			alreadyWithComment = False

			for currentLineId in range(0, lines):
				if not alreadyWithComment:
					currentLine = content[currentLineId]
					print ("evaluating:", currentLine)
					if (currentLine.startswith("// " + parameter)):
						print ("comment found (file already marked properly)")
						alreadyWithComment = True
						break

			if not alreadyWithComment:
				# add comment to file content
				newContent = ["// " + parameter]
				for entry in content:
					newContent.append(entry)

				# open file for writing
				handle = open(parameter, "w")

				print (newContent)
				for line in newContent:
					handle.write(line)

				print ("comment added (file marked properly)")

				# close file
				handle.close()

	currentArg += 1



