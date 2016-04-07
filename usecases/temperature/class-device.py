# -----------------------------------------------------------
# a class to setup a temperature measurement device
#
# requires Python 3.x:
# python3 class-device.py
#
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------
#

# device class

class Device:
	def __init__(self, temp = 0.0, unit = True):
		"constructor for this object"
		
		# init the temperature
		self.temperature = float(temp)
		
		# unit: True (Celsius), False (Fahrenheit)
		self.measurement = unit
		
		return
	
	def getTemperature (self):
		"return the temperature"
		return self.temperature
	
	def setTemperature (self, temp):
		"set the temperature value"
		self.temperature = float(temp)
		return
	
	def setUnit (self, unit = True):
		"set the measurement unit"
		self.measurement = unit
		return

	def getUnit (self):
		"return the measurement unit"
		
		# unit: True (Celsius), False (Fahrenheit)
		return self.measurement
	
	def getCelsius (self):
		"transform the temperature value into Celsius"
		
		if self.isUnitCelsius ():
			return self.getTemperature ()
		else:
			celsius = (self.getTemperature - 32.0) * 5.0 / 9.0
			return celsius
	
	def isUnitFahrenheit (self):
		"return True if the device unit is set to Fahrenheit"
		if not self.getUnit():
			return True
		
		return False

	def isUnitCelsius (self):
		"return True if the device unit is set to Celsius"
		if self.getUnit():
			return True
		
		return False

	def getFahrenheit (self):
		"transform the temperature value into Fahrenheit"
		
		if self.isUnitFahrenheit ():
			return self.getTemperature ()
		else:
			fahrenheit = (self.getTemperature() * 9.0) / 5.0 + 32.0
			return fahrenheit

# main program
if __name__ == "__main__":
	# define a device with 20.5 degree celsius
	myDevice = Device(20.5, True)
	
	temperatureCelsius = myDevice.getCelsius()
	temperatureFahrenheit = myDevice.getFahrenheit()

	print ("device: %.2f °C" % (temperatureCelsius))
	print ("device: %.2f °F" % (temperatureFahrenheit))

