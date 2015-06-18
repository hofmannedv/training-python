
# define filename to work with
filename = "/etc/passwd"

# open file and read content
fileId = open(filename)
content = fileId.readlines()

# close file
fileId.close()

# define empty list of user names
usernames = []

# go through the lines one after the other
for line in content:
	# split line by ":" into single fields
	fields = line.split(":")

	#print (fields)
	# extract user name
	currentName = fields[0]
	# extend list of usernames
	usernames.append(currentName)

print (sorted(usernames))
