# -----------------------------------------------------------
# demonstrates the definition and usage of bright ansi colors
#o
# (C) 2016-2026 Frank Hofmann, Freiburg/Berlin, Germany
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# 
# follows the techniques as described in Haoyi's Programming Blog:
# http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# -----------------------------------------------------------

# define color set
brightColorSet = {
	"brightBlack": "\u001b[30;1m",
	"brightRed": "\u001b[31;1m",
	"brightGreen": "\u001b[32;1m",
	"brightYellow": "\u001b[33;1m",
	"brightBlue": "\u001b[34;1m",
	"brightMagenta": "\u001b[35;1m",
	"brightCyan": "\u001b[36;1m",
	"brightWhite": "\u001b[37;1m"
}

# define reset code
resetCode = "\u001b[0m"

for item in brightColorSet:
	print ("%s %s" % (brightColorSet[item],item))

print (resetCode)
