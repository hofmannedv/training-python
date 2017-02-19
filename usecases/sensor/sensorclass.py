
# -----------------------------------------------------------
# defines a Sensor class
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

class Sensor:

	# define a list of captured data
	data = []

	def __init__ (self):
		"initialize the Sensor object"
		self.data = []
		return
	
	def getData (self, dateFrom, dateTo):
		"return the captured sensorValue in the specified time range"
		
		# define empty dataset
		outputDataset = []
		
		# go through the captured data
		for dataset in self.data:
			if dataset["timestamp"] <= dateTo:
				if dataset["timestamp"] >= dateFrom:
					outputDataset.append(dataset)
		
		return outputDataset
	
	def addData (self, timestamp, sensorValue):
		"add captured data"
		dataset = {
			"timestamp": timestamp,
			"value": sensorValue
		}
		self.data.append(dataset)
		return

