# -----------------------------------------------------------
# demonstrates how to validate a variable for being an object
# inherited from a certain class
#o
# (C) 2017 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

class Point:
	def __init__(self, x, y):
		"constructor to initiate this object"

		# store the coordinates
		self.x, self.y = x, y
		
		return
	
	def getX(self):
		"method to return the x coordinate"
		return self.x
	
	def getY(self):
		"method to return the y coordinate"
		return self.y
	
# main program

# create three single nodes
point1 = Point(1,5)
point2 = Point(25,4)
point3 = [5,10]

# create list of tracks
track = [point1, point2, point3]

for position in track:
	if isinstance(position, Point):
		print("position at %i,%i" % (position.getX(),position.getY()))
	else:
		print("position: invalid data structure")
