# -----------------------------------------------------------
# demonstrates the definition and usage of ansi colors
#o
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
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

for item in basicColorSet:
	print ("%s %s" % (basicColorSet[item],item))

print (resetCode)
