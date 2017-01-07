#!/usr/bin/python

import fileinput
import re
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

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

travelRoutes = np.array([])

for entry in data[1:]:
	route = np.array("%s->%s:%s" % (entry[2], entry[3], entry[4]))
	travelRoutes = np.hstack((travelRoutes, route))

travelRoutes = np.unique(travelRoutes)
print (travelRoutes)

monate = monthlyRanges[1:, 0:1]

anzahl = np.zeros((travelRoutes.size, monate.size), dtype = np.int32)
print (anzahl)

for entry in data[1:]:
	route = np.array("%s->%s:%s" % (entry[2], entry[3], entry[4]))
	travelRouteId = np.where(travelRoutes == route)[0][0]

	travelRouteDateFrom = entry[0]
	travelRouteDateTo = entry[1]

	monthId = 0
	for entry in monthlyRanges[1:]:
		monthDateFrom = datetime.strptime(entry[1], '%Y-%m-%d %H:%M:%S')
		monthDateTo = datetime.strptime(entry[2], '%Y-%m-%d %H:%M:%S')

		if ((travelRouteDateFrom >= monthDateFrom) and (travelRouteDateFrom <= monthDateTo)):
			if ((travelRouteDateTo >= monthDateFrom) and (travelRouteDateTo <= monthDateTo)):
				anzahl[travelRouteId][monthId] += 1
				break
		monthId += 1
print (anzahl)

distances = np.array([])
entryId = 0
pdi = []
for entry in travelRoutes:
	kmx = np.zeros(12)
	spalten = re.split(':', entry)
	factor = int(spalten[1])
	
	for i in range(12):
		kmx[i] = anzahl[entryId][i] * factor
	distances = np.append(distances, [kmx])
	entryId += 1

	pdi.append(spalten[0])

distances = np.reshape(distances, (travelRoutes.size,monate.size))
distances = distances.swapaxes(1,0)

df = pd.DataFrame(distances,
               index=monate,
               columns=pd.Index(pdi))
df.plot(kind='barh', stacked=True)
plt.show()
