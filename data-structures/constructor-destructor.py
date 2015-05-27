# -----------------------------------------------------------
# a class to demonstrate object constructor and destructor
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------
#

# class definition

class Point:
	def __init__(self, latitude, longitude, nodeName):
		"""
		init the object (constructor)
		"""
		
		# set coordinates
		self.latitude = latitude
		self.longitude = longitude
		
		# set point name
		self.name = nodeName
		
		# output status message
		print ("Point %s object initialized" % self.name)
		return
	
	def __del__(self):
		"""
		clean the object (destructor)
		"""
		
		# output status message
		print ("Point %s object deleted" % self.name)
		return

# main program
if __name__ == "__main__":
	# define three slightly different points
	point1 = Point(4.3, 17.4, "A")
	point2 = Point(12.0, 8.2, "B")
	point3 = Point(6.7, 0.3, "C")
	
	# long loop
	a = 1
	for i in range(100000):
		if a == 35:
			# explicit deletion of point 1
			del point1
		if a == 3000:
			# explicit deletion of point 2
			del point2
		if a == 7777:
			# explicit deletion of point 3
			del point3
