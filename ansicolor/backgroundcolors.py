# -----------------------------------------------------------
# demonstrates the definition and usage of ansi colors (background)
#o
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# follows the techniques as described in Haoyi's Programming Blog:
# http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# -----------------------------------------------------------

# define basic background color set
backgroundColorSet = {
	"black": "\u001b[40m",
	"red": "\u001b[41m",
	"green": "\u001b[42m",
	"yellow": "\u001b[43m",
	"blue": "\u001b[44m",
	"magenta": "\u001b[45m",
	"cyan": "\u001b[46m",
	"white": "\u001b[47m"
}

# define bright background color set
backgroundBrightColorSet = {
	"black": "\u001b[40;1m",
	"red": "\u001b[41;1m",
	"green": "\u001b[42;1m",
	"yellow": "\u001b[43;1m",
	"blue": "\u001b[44;1m",
	"magenta": "\u001b[45;1m",
	"cyan": "\u001b[46;1m",
	"white": "\u001b[47;1m"
}

# define reset code
resetCode = "\u001b[0m"

for item in backgroundColorSet:
	# output the basic version
	print ("%s %s " % (backgroundColorSet[item],item))

for item in backgroundBrightColorSet:
	# output the bright version
	print ("%s %s " % (backgroundBrightColorSet[item],item))

print (resetCode)
