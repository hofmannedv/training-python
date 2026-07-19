# -----------------------------------------------------------
# demonstrates the definition and usage of ansi colors
#o
# (C) 2016-2026 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# follows the techniques as described in Haoyi's Programming Blog:
# http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# -----------------------------------------------------------

# define color set
basicColorSet = {
	"black": "\u001b[30m",
	"red": "\u001b[31m",
	"green": "\u001b[32m",
	"yellow": "\u001b[33m",
	"blue": "\u001b[34m",
	"magenta": "\u001b[35m",
	"cyan": "\u001b[36m",
	"white": "\u001b[37m"
}

# define reset code
resetCode = "\u001b[0m"

# print text in the corresponding colour
for item in basicColorSet:
	print ("%s %s" % (basicColorSet[item],item))

# reset the colour to the initial state
print (resetCode)
