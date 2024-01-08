# -----------------------------------------------------------
# demonstrates the definition and usage of ansi colors
# using the colorama library
# https://pypi.org/project/colorama/
#
# (C) 2024 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

from colorama import Fore, Style

# define color set
basicColorSet = {
	"black": Fore.BLACK,
	"red": Fore.RED,
	"green": Fore.GREEN,
	"yellow": Fore.YELLOW,
	"blue": Fore.BLUE,
	"magenta": Fore.MAGENTA,
	"cyan": Fore.CYAN,
	"white": Fore.WHITE
}

# define reset code
resetCode = Style.RESET_ALL

# print text in the corresponding colour
for item in basicColorSet:
	print ("%s %s" % (basicColorSet[item],item))

# reset the colour to the initial state
print (resetCode)
