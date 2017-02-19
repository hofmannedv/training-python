#!/usr/bin/python

# -----------------------------------------------------------
# validates sensor data using a Sensor class
# outputs the data as a csv file
# demonstrates the usage of the datetime, and csv module
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import datetime, csv
from sensorclass import Sensor

# define temperature sensor
temperatureSensor = Sensor()

# insert data
temperatureList = [
	[datetime.date(2017,1,1), 25],
	[datetime.date(2017,1,2), 21],
	[datetime.date(2017,1,3), 18],
	[datetime.date(2017,1,4), 27]
]
for entry in temperatureList:
	timestamp, value = entry
	temperatureSensor.addData(timestamp, value)

# define wind sensor
windSensor = Sensor()

# insert data
windList = [
	[datetime.date(2017,1,1), 14],
	[datetime.date(2017,1,2), 5],
	[datetime.date(2017,1,3), 164],
	[datetime.date(2017,1,4), 45]
]
for entry in windList:
	timestamp, value = entry
	windSensor.addData(timestamp, value)

# output a table holding all the captured date in a time range
print("%30s: %15s %10s" % ("Date", "Temperature", "Wind"))
with open('data.log', 'w', newline='\n') as csvfile:
	dataWriter = csv.writer(csvfile, delimiter=':')
	
	for day in [1,2,3]:
		# define start and end date
		startDate = datetime.date(2017,1, day)
		endDate = datetime.date(2017,1, day)
		
		# retrieve data: one entry per day
		temperatureData = temperatureSensor.getData(startDate, endDate)
		print (temperatureData)
		windData = windSensor.getData(startDate, endDate)
	
		# output entry
		timestamp = startDate.strftime("%A, %d. %B %Y")
		temperature = temperatureData[0]["value"]
		wind = windData[0]["value"]
		print("%30s: %15s %10s" % (timestamp, temperature, wind))
		
		dataWriter.writerow([timestamp, temperature, wind])
