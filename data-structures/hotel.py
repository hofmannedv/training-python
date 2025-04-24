# !/usr/bin/python

# -----------------------------------------------------------
# demonstrates how to write a Hotel class 
#o
# (C) 2018-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

class Hotel:

    hotelName = ""
    hotelRooms = 0
    hotelPlace = ""

    def __init__(self, name, rooms, place):
        "initialize the Hotel class object"
        self.hotelName = name
        self.hotelRooms = rooms
        self.hotelPlace = place
        return

    def getRooms(self):
        "return the number of rooms"
        return self.hotelRooms

    def getHotelName(self):
        "return the hotel name"
        return self.hotelName

    def getPlace(self):
        "return the place of the hotel"
        return self.hotelPlace

    def __eq__(self, other):
        "compare the attributes for being equal"
        if self.getRooms() == other.getRooms():
            #print ("rooms are similar")
            if self.getHotelName() == other.getHotelName():
                #print("hotel name is similar")
                if self.getPlace() == other.getPlace():
                    #print("place is similar")
                    return True
        return False
    
    def __str__(self):
        "print a short info about the Hotel"
        return ("the %s in %s has %i rooms" % (self.getHotelName(), self.getPlace(), self.getRooms()))

hotel1 = Hotel ("Grand Hotel", 200, "Paris")
hotel2 = Hotel ("Chateau Rouge", 15, "Dijon")
hotel3 = Hotel ("Auberge de la Marine", 15, "Bordeaux")
hotel4 = Hotel ("Chateau Rouge", 15, "Dijon")

currentList = [hotel1, hotel2, hotel3, hotel4]

print ("original hotel list:")
for entry in currentList:
    print (entry)

adjustedList = []

for entry in currentList:
    if adjustedList == []:
        adjustedList.append(entry)
        print("added:")
        print(entry)
    else:
        notFound = True
        for item in adjustedList:
            if entry == item:
                notFound = False
                break
        if notFound:
            adjustedList.append(entry)
            print("added:")
            print(entry)

print ("adjusted hotel list:")
for entry in adjustedList:
    print (entry)

