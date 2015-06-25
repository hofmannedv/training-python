# -----------------------------------------------------------
# demonstrates how to work with sax module to extract xml 
# fields
#
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard modules
from xml.sax import make_parser, handler
import re

# define a class to work with podcast data
class podcastHandler(handler.ContentHandler):

	def startElement(self, name, attrs):

		pattern = "enclosure"
		prog = re.compile(pattern)

		if re.match(prog, name):
			print (name)
			print (attrs.get("url", ""))
			print (attrs.get("length", ""))

		return

# define podcat parser
parser = make_parser()

# attach podcast handler
p = podcastHandler()
parser.setContentHandler(p)

# extract data
parser.parse("hackerfunkfeed.xml")
