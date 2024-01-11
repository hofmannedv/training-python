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

from colorama import Fore, Back, Style

# define foreground, and background colour
foreground = Fore.WHITE
background = Back.BLUE

# define bold flag
bold = Style.BRIGHT

# define reset code
resetCode = Style.RESET_ALL

# define text
textNormal = " white on blue        "
textBold =   " white on blue (bold) "

# output text 
print ("%s%s%s" % (background, foreground, textNormal))
print ("%s%s%s%s" % (background, bold, foreground, textBold))

# reset the colour to the initial state
print (resetCode)
