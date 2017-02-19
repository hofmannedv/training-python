
#!/usr/bin/python

# -----------------------------------------------------------
# validates an International Bank Account Number (IBAN) using 
# a Regular Expression
# demonstrates the usage of the re module
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import re

def validateIban(iban):
	"validates an International Bank Account Number (IBAN) using a Regular Expression"
	
	# define the pattern
	pattern = re.compile("^[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16}$")
	
	# validate the pattern
	if re.match(pattern, iban):
		return True
	else:
		return False

# define IBAN dataset
listOfIbans = [
	"DE85370100500123456503",
	"DE56752500000021114251",
	"CH1887050500178114RX55",
]

for iban in listOfIbans:
	if validateIban(iban):
		print("IBAN %s is valid" % iban)
	else:
		print("IBAN %s is not valid" % iban)

