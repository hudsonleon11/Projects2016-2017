'''
password.py - check user and password 4 times
hudson.leon - intial coding January 31
'''

#imports

#functions
def authenticateMe(user,password,secretuser,secretpass):
	if (user == secretuser and password == secretpass):
		return True
	else:
		return False


#main code

#1. set secret user and password
secretUser = "joe"
secretPass = "blow"

#2. ask user to authenticate - give them 4 tries

for i in range(4):
	user = raw_input("Enter your user name: ")
	password = raw_input("Enter your password: ")
	if (i == 3):
		print "You have attempted to log in 4 times. Your account is locked."
	elif (authenticateMe(user,password,secretUser,secretPass) == True):
		print "Welcome, you have been authenticated as a trusted user"
		break # this terminates the current loopand resumes at the next statement 
	else:
		print "Incorrect credentials. Try again"
