#!/usr/bin/python

import fileinput
import re
from datetime import datetime

# import external NumPy module
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

init = True

# preparing the data

for line in fileinput.input():
	line = re.sub('\n', '', line)
	columns = re.split('\t+', line)
	if init:
		data = np.array([columns])
		init = False
	else:
		columns[0] = datetime.strptime(columns[0], '%Y-%m-%d %H:%M:%S')
		columns[1] = datetime.strptime(columns[1], '%Y-%m-%d %H:%M:%S')
		data2 = np.array([columns])
		data = np.vstack((data, data2))

monthlyRanges = np.array([
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
])

# define travel routes
travelRoutes = np.array([])

for entry in data[1:]:
	route = np.array("%s->%s:%s" % (entry[2], entry[3], entry[4]))
	travelRoutes = np.hstack((travelRoutes, route))

# remove double entries
travelRoutes = np.unique(travelRoutes)
# print (travelRoutes)

# extract descriptions for every month
month = monthlyRanges[1:, 0:1]
month = np.ravel(month)
# print (month)

# define number of travels per month
# - init with zeros
numberOfTravels = np.zeros((travelRoutes.size, month.size), dtype = np.int32)
# print (numberOfTravels)

for entry in data[1:]:
	# find list id for the travel route
	route = np.array("%s->%s:%s" % (entry[2], entry[3], entry[4]))
	travelRouteId = np.where(travelRoutes == route)[0][0]

	# extract travel data
	travelRouteDateFrom = entry[0]
	travelRouteDateTo = entry[1]

	monthId = 0
	for entry in monthlyRanges[1:]:
		# extract month data range
		monthDateFrom = datetime.strptime(entry[1], '%Y-%m-%d %H:%M:%S')
		monthDateTo = datetime.strptime(entry[2], '%Y-%m-%d %H:%M:%S')

		# validate route for being in month range
		if ((travelRouteDateFrom >= monthDateFrom) and (travelRouteDateFrom <= monthDateTo)):
			if ((travelRouteDateTo >= monthDateFrom) and (travelRouteDateTo <= monthDateTo)):
				numberOfTravels[travelRouteId][monthId] += 1
				break
		monthId += 1
# print (numberOfTravels)

# define distance per entry
distances = np.array([])
entryId = 0
travelDescription = []
for entry in travelRoutes:
	columns = re.split(':', entry)
	factor = int(columns[1])
	
	distances = np.append(distances, [numberOfTravels[entryId] * factor])
	entryId += 1

	travelDescription.append(columns[0])

# re-arrange the distances array
distances = np.reshape(distances, (travelRoutes.size,month.size))
distances = distances.swapaxes(1,0)

# create data frame
df = pd.DataFrame(distances,
               index=month,
               columns=pd.Index(travelDescription))

# plot the data frame as stacked, horizontal bars
df.plot(kind='barh', stacked=True)

# display the data frame
plt.show()
