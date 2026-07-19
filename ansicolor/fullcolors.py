# -----------------------------------------------------------
# demonstrates the definition and usage of 256 ansi colors
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

import sys

# define reset code
resetCode = "\u001b[0m"

# output 16 lines
for i in range(0, 16):
	# output 16 colors per line
	for j in range(0, 16):
		code = str(i * 16 + j)
		sys.stdout.write("\u001b[38;5;" + code + "m " + code.rjust(4))
	
	# reset code
	print (resetCode)

