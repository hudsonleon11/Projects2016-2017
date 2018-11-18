#ssrgmio.py - python prog, to prove compliance
#hudson.leon - Nov. 24, 2016 - initial coding
#---------------------------------------------

#import


# function area
def times(firstnum,secondnum):
	product = firstnum * secondnum
	return product

# main code area 
num = 17 
print (num)  

if (num > 7):
	for i in range(num):	
		print ("greater than")
elif (num < 7):
	print ("less than")
else: 
	print ("number isssss 7") 

print times(10,5) 
# call the function and print what is returned

#read in from file
filein = open("data.txt","r")
namelist = filein.readlines()
print(namelist)
filein.close()

#

