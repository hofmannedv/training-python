# -----------------------------------------------------------
# demonstrates the definition and usage of ansi colors (background)
# using the colorama library
# https://pypi.org/project/colorama/
#
# (C) 2024 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

from colorama import Back, Style

# define basic background color set
backgroundColorSet = {
	"black": Back.BLACK,
	"red": Back.RED,
	"green": Back.GREEN,
	"yellow": Back.YELLOW,
	"blue": Back.BLUE,
	"magenta": Back.MAGENTA,
	"cyan": Back.CYAN,
	"white": Back.WHITE
}

# define reset code
resetCode = Style.RESET_ALL

for item in backgroundColorSet:
	# output the basic version
	print ("%s %s " % (backgroundColorSet[item],item))

print (resetCode)
