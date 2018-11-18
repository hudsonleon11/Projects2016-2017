''' trianglprob.py - junior problem #1 2014
'''

# imports

# functions
def kindoftriangle(angle1,angle2,angle3):
	if ((angle1 + angle2 + angle3) != 180):
		return ("Error")
	elif (angle1 == angle2 and angle2 == angle3):
		return "Equilateral"
	elif (angle1 == angle2 or angle2 == angle3): 
		return "Isosoles"
	else:
		return "Scalene"
# main code
angle1 = input("enter first angle:") 
angle2 = input("enter second angle:") 
angle3 = input("enter third angle:")

print kindoftriangle(angle1,angle2,angle3)
 
