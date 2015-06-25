# -----------------------------------------------------------
# find similar entries in /etc/passwd
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------
#

# import random module
import random

# define specific user class
class UserDingsbums:

	def __init__(self):
		self.login = ""
		self.uid = ""
		self.gid = ""
		self.gecos = "" 
		self.homedir = ""
		self.shell = ""
		return

	def extractPasswdFields(self,line):
		
		# split line by ":" into single fields
		fields = line.split(":")

		self.login = fields[0]
		self.password = fields[1]
		self.uid = fields[2]
		self.gid = fields[3]
		self.gecos = fields[4]
		self.homeDir = fields[5]
		self.shell = fields[6]

		return

	def constructPasswordFields(self):
		fields = self.login + ":" + self.password + ":" + self.uid + ":" + self.gid + ":" + self.gecos + ":" + self.homeDir + ":" + self.shell
		return fields

	def getLogin(self):
		return self.login

	def getUid(self):
		return self.uid

	def __eq__(self, referenceObject):
		return self.getLogin() == referenceObject.getLogin() and \
               self.getUid() == referenceObject.getUid()

# define filename to work with
filename = "/etc/passwd"

# open file and read content
fileId = open(filename)
content = fileId.readlines()

# close file
fileId.close()

# define empty list of user names
userData = {}

objectList = []

# go through the lines one after the other
for line in content:

	# create object
	userObject = UserDingsbums()

	# read line
	userObject.extractPasswdFields(line)

	# extend object list
	objectList.append(userObject)

referenceObject = random.choice(objectList)

for currentObject in objectList:
	if currentObject == referenceObject:
		print ("identisches Objekt:", referenceObject, currentObject)
		print (currentObject.getLogin())
		print (currentObject.getUid())

outputFileContent = []
for currentObject in objectList:
	outputFileContent.append(currentObject.constructPasswordFields())

# define filename to output data
filename = "/tmp/x.data"

# open file and read content
fileId = open(filename, "w")
fileId.writelines(outputFileContent)

# close file
fileId.close()

