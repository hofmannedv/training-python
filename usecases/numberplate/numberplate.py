
#!/usr/bin/python

# -----------------------------------------------------------
# validates a number/license plate using a Regular Expression
# demonstrates the usage of the re module
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import re

class Vehicle:

	name = ""
	licenseNumber = ""

	def __init__ (self, name, licenseNumber):
		"initiates the Vehicle object"
		self.name = name
		self.licenseNumber = licenseNumber
		return

	def getName (self):
		"return the name of the car"
		return self.name

	def getLicenseNumber (self):
		"return the number of the license plate"
		return self.licenseNumber

# define vehicles
vehicle1 = Vehicle("Ferrari 308 GTS", "GE 16744")
vehicle2 = Vehicle("VW Scirocco", "F-K1865")
vehicle3 = Vehicle("Talbot-Simca 1100", "B-TS1556H")
vehicle4 = Vehicle("Delahaye Tourer 1925", "3809 MB 76")

# define patterns for license number schemes
patternCh = re.compile("^[A-Z]{2}\ \d{1,6}$")
patternGe = re.compile("^[A-Z]{1,3}-[A-Z]{1,2}\d{1,4}$")
patternGeHistoric = re.compile("^[A-Z]{1,3}-[A-Z]{1,2}\d{1,4}H$")

for vehicle in [vehicle1, vehicle2, vehicle3, vehicle4]:
	# retrieve name and license plate
	name = vehicle.getName()
	licensePlate = vehicle.getLicenseNumber()
	print ("the vehicle %s has the license number %s" % (name, licensePlate))
	
	# authority check
	if re.match(patternCh, licensePlate):
		print("registered in Switzerland")
	elif re.match(patternGe, licensePlate):
		print("registered in Germany")
	elif re.match(patternGeHistoric, licensePlate):
		print("registered in Germany as oldtimer")
	else:
		print("registration authority unknown")
