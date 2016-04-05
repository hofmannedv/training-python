# -----------------------------------------------------------
# a class to setup a temperature measurement device
#
# requires Python 3.x
#
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------
#

# device class

class Device:
	def __init__(self, temp = 0, unit = True):
		"constructor for this object"
		
		# init the temperature
		self.temperature = temp
		
		# unit: True (Celsius), False (Fahrenheit)
		self.measurement = unit
		
		return
	
	def getTemperature (self):
		"return the temperature"
		return self.temperature
	
	def setTemperature (self, temp):
		"set the temperature value"
		self.temperature = temp
		return
	
	def getUnit (self):
		"return the measurement unit"
		
		# unit: True (Celsius), False (Fahrenheit)
		return self.measurement

# main program
if __name__ == "__main__":
	# define a device
	myDevice = Device(20, True)
	
	temperature = myDevice.getTemperature()
	unit = "°F"
	if myDevice.getUnit:
		unit = "°C"

	print ("device: %i %s" % (temperature, unit))

