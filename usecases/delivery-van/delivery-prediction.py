# -----------------------------------------------------------
# predict a schedule for a delivery van using the geopy module
# and Nominatim
#o
# A delivery van is given a list of delivery addresses, which 
# it visits one after the other. A 10-minute waiting and loading 
# time is allowed for each address. The delivery van travels the 
# route at an average speed of 55 km per hour and arrives at the 
# first delivery address at 8 am. The aim is to calculate the 
# estimated times at which it will arrive at the other delivery 
# addresses and when the journey will be completed.
#
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define the required modules
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import datetime

def calculateDistance(geolocator, place1, place2):
    # send a request to Nominatim: translate name to coordinates
    location1 = geolocator.geocode(place1)
    location2 = geolocator.geocode(place2)

    # send a request to Geodesic: calculate distance
    distance = geodesic(
        (location1.latitude,location1.longitude),
        (location2.latitude,location2.longitude)
    ).km

    return float(distance)

deliveryPoints = [
    "Muensterplatz Freiburg",
    "Bergstation Schauinsland",
    "Todtnauer Wasserfall, Todtnau",
    "Dreiländerbrücke, Weil am Rhein",
    "Schloss Biederthal, Burg im Leimental",
    "Maison de la Tête de Moine, Bellelay",
    "Weissenstein, Solothurn"
]

# define geolocator from Nominatim
geolocator = Nominatim(user_agent="myName")

# define timestamp today 8h00
startTime = datetime.datetime.today() 
startTime = startTime.replace(hour=8, minute=0, second=0)

travelPlan = []
totalDistance = 0
position = 0
while position < len(deliveryPoints) - 1:
    start = deliveryPoints[position]
    end = deliveryPoints[position + 1]
    distance = calculateDistance(geolocator, start, end)
    print("von %s -> %s" % (start, end))

    part = [start, end, distance]
    travelPlan.append(part)

    totalDistance = totalDistance + distance
    position = position + 1 

    # calculate travel time
    travelTime = int((distance / 55) * 60)
    timeDifference = datetime.timedelta(minutes=travelTime)
    # print(timeDifference)

    # calculate arrival time
    arrivalTime = startTime + datetime.timedelta(minutes=travelTime)

    # output track info
    print(startTime.strftime("%H:%M:%S") + " -> " + arrivalTime.strftime("%H:%M"))

    # wait for 10 minutes
    startTime = arrivalTime + datetime.timedelta(minutes=10)

print("Total travel distance: %i km" % totalDistance)
print("Arrival time at destination:", arrivalTime.strftime("%H:%M"))
