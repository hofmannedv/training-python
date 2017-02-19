
#!/usr/bin/python

# -----------------------------------------------------------
# validates an IPv4 address using a Regular Expression
# demonstrates the usage of the re module
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import re

pattern = re.compile("^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
hosts = ["10.10.35.10", "1.2.3.4.5", "255.255.255.0", "654.324.11.8"]

for ip in hosts:
	if re.match(pattern,ip):
		print("%s is a valid ipv4 address" % ip)
	else:
		print("%s is not a valid ipv4 address" % ip)
