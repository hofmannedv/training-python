# -----------------------------------------------------------
# find similar entries in /etc/passwd
# demonstrate the definition and usage of classes
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
		# initiate the entry fields of /etc/passwd
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

		# associate the fields
		self.login = fields[0]
		self.password = fields[1]
		self.uid = fields[2]
		self.gid = fields[3]
		self.gecos = fields[4]
		self.homeDir = fields[5]
		self.shell = fields[6]

		return

	def constructPasswordFields(self):
		# concatenate the single fields by ":"
		fieldSet = (self.login, self.password, self.uid, self.gid, self.gecos, self.homeDir, self.shell)
		fields = ":".join(fieldSet)
		return fields

	def getLogin(self):
		# return the login name
		return self.login

	def getUid(self):
		# return the user id
		return self.uid

	def getGroupId(self):
		# return the group id
		return self.gid

	def __eq__(self, referenceObject):
		# compare two objects, and return True if they are similar in
		# terms of its login name, and its user id
		return self.getLogin() == referenceObject.getLogin() and \
               self.getUid() == referenceObject.getUid()

# define filename to work with
filename = "/etc/passwd"

# open file and read content
fileId = open(filename)
content = fileId.readlines()

# close file
fileId.close()

# define an empty list of user names
userData = {}

# define an empty list of objects
objectList = []

# go through the lines one after the other
for line in content:

	# create a new object
	userObject = UserDingsbums()

	# read line
	userObject.extractPasswdFields(line)

	# extend object list
	objectList.append(userObject)

# choose an random object from the list of objects
referenceObject = random.choice(objectList)

# go through the list one by one
for currentObject in objectList:
	if currentObject == referenceObject:
		print ("identisches Objekt:", referenceObject, currentObject)
		print (currentObject.getLogin())
		print (currentObject.getUid())

# create an output file -- prepare its content
outputFileContent = []
for currentObject in objectList:
	outputFileContent.append(currentObject.constructPasswordFields())

# define the name of the output file
filename = "/tmp/x.data"

# open file for writing, and save the content
fileId = open(filename, "w")
fileId.writelines(outputFileContent)

# close file
fileId.close()

