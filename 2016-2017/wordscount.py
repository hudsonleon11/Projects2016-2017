'''
banner
'''

# imports
# functions

# funcion to find longest word and return it to the calling line
def findlong(fi):
	longword = ""
	longwordlen = 0
	for word in fi:
		if (len(word) > longwordlen):
			longword = word
			longwordlen = len(word)
	return longword
	return longwordlen
#main code

# ecception or error handling try/except
try:
	file = open("german.txt","r") #open file into variable - read only
except:
	print "can not find the file" #error check for run time error

#calls function to find logest word and number of letters
longword = findlong(file)
print longword
print len(longword)
