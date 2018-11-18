'''
sleepin.py - program to help you decide to sleep in or not
Jan 21, 2017 - original coding, hudson.leon. adapted from codingbat.com Warmup-1
'''
#code section 1# - imports -----------------------------------------------

#code section 2# - functions ---------------------------------------------

#blackbox function that recieves string data, makes decision and returns boolean answer
def sleep_in(weekday, vacation):
	if (weekday == "no" or  vacation == "yes"):
		return True
	else:
		return False

# code section 3# - main code area ---------------------------------------

#get string input from user
weekday = raw_input("Is it a weekday? (type yes, or no):" )
vacation = raw_input("Is it a vacation? (type yes or no): " )

# call a function, pass in input and store output in a boolean variable
sleeping = sleep_in(weekday,vacation)
#check output from function and print appropriate message to the screen
if (sleeping == True):
	print ("feel free to sleep in")
else:
	print ("get up lazy bones!") 

