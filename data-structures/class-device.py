# -----------------------------------------------------------
# a class to setup a measurement device with GPS coordinates
#o
# (C) 2015-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------
#

# device class

class Device:
	def __init__(self, latitude, longitude, salinity, name):
		"constructor for this object"
		
		# coordinates: longitude, and latitude
		self.longitude = longitude
		self.latitude = latitude
		
		# salinity
		self.salinity = salinity
		
		# name of the device
		self.name = name
	
	def getPosition (self):
		"return the position"
		position = (self.latitude, self.longitude)
		return position
	
	def setSalinity (self, salinity):
		"set the salinity value"
		self.salinity = salinity
		return
	
	def getSalinity (self):
		"return the salinity value"
		return self.salinity
	
	def getName (self):
		"return the device name"
		return self.name
	
	def __eq__ (self, referenceObject):
		"""
		overload the eq operator to compare two objects
		"""
		return self.latitude == referenceObject.latitude and self.longitude == referenceObject.longitude
	
# main program
if __name__ == "__main__":
	# define three slightly different devices
	myDevice = Device(45.5, 17.4, 0.5, "Rhodos")
	myDevice2 = Device(13.2, 1.5, 0.6, "Kreta")
	myDevice3 = Device(13.2, 1.5, 0.6, "Kreta2")
	
	# process the devices as a list
	for i in myDevice, myDevice2, myDevice3:
		# output device name, position, and salinity
		print (i.getName(), ":", i.getPosition(), "salinity:", i.getSalinity())
	
	# compare two devices
	if myDevice2 == myDevice3:
		print ("devices 2 and 3 are equal")

