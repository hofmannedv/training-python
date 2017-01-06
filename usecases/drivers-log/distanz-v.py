#!/usr/bin/python

import fileinput
import re
from datetime import datetime

# import external NumPy module
import numpy as np

init = True

# preparing the data

for zeile in fileinput.input():
	zeile = re.sub('\n', '', zeile)
	spalten = re.split('\t+', zeile)
	if init:
		data = np.array([spalten])
		init = False
	else:
		spalten[0] = datetime.strptime(spalten[0], '%Y-%m-%d %H:%M:%S')
		spalten[1] = datetime.strptime(spalten[1], '%Y-%m-%d %H:%M:%S')
		data2 = np.array([spalten])
		data = np.vstack((data, data2))

monthlyRanges = [
	['Ganzes Jahr', '2017-01-01 00:00:00', '2017-12-31 23:59:59'],
	['Januar',      '2017-01-01 00:00:00', '2017-01-31 23:59:59'],
	['Februar',     '2017-02-01 00:00:00', '2017-02-28 23:59:59'],
	['März',        '2017-03-01 00:00:00', '2017-03-31 23:59:59'],
	['April',       '2017-04-01 00:00:00', '2017-04-30 23:59:59'],
	['Mai',         '2017-05-01 00:00:00', '2017-05-31 23:59:59'],
	['Juni',        '2017-06-01 00:00:00', '2017-06-30 23:59:59'],
	['Juli',        '2017-07-01 00:00:00', '2017-07-31 23:59:59'],
	['August',      '2017-08-01 00:00:00', '2017-08-31 23:59:59'],
	['September',   '2017-09-01 00:00:00', '2017-09-30 23:59:59'],
	['Oktober',     '2017-10-01 00:00:00', '2017-10-31 23:59:59'],
	['November',    '2017-11-01 00:00:00', '2017-11-30 23:59:59'],
	['Dezember',    '2017-12-01 00:00:00', '2017-12-31 23:59:59']
]

for currentMonth in monthlyRanges:
	month, dateFrom, dateTo = currentMonth
	dateFromI = datetime.strptime(dateFrom, '%Y-%m-%d %H:%M:%S')
	dateToI = datetime.strptime(dateTo, '%Y-%m-%d %H:%M:%S')
	print (" ")
	print ("----------------------------------------------------")
	print (month, dateFromI, dateToI)
	print ("----------------------------------------------------")
	
	fromColumn = np.array(data[1:,0:1])
	toColumn = np.array(data[1:,1:2])
	mask = (fromColumn >= dateFromI) & (toColumn < dateToI)
	
	if mask.any():
		# convert mask into list
		newFilter = mask.ravel()
		stripe = np.compress(newFilter, data[1:], axis=0)
		
		# calculate the total travelling distance
		# - select the 5th column except the 1st row
		# - convert strings into 32bit integer
		distanceColumn = np.array(stripe[:,4], dtype=np.int32)
		
		# count the distances
		total = np.sum(distanceColumn)
		print ("Gesamt          : %i km" % (total))
		
		# count number of travels
		number = np.size(distanceColumn)
		print ("Anzahl Fahrten  : %i" % (number))
		
		# find shortest travel
		shortest = np.argmin(distanceColumn)
		shortestFrom = stripe[shortest][2]
		shortestTo = stripe[shortest][3]
		shortestDistance = stripe[shortest][4]
		print ("Kürzeste Strecke: %s nach %s mit %s km" % (shortestFrom, shortestTo, shortestDistance))
		
		# find longest travel
		longest = np.argmax(distanceColumn)
		longestFrom = stripe[longest][2]
		longestTo = stripe[longest][3]
		longestDistance = stripe[longest][4]
		print ("Längste Strecke : %s nach %s mit %s km" % (longestFrom, longestTo, longestDistance))

