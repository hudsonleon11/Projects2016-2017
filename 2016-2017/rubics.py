#-------------------
#rubics.py
#hudsonleon - Nov 26, 2016 - intial programming 

#imports
import turtle
import random 


#functions
def shape(myturtle,length,sides,angle):
	myturtle.color(getRGB())
	for i in range(sides):
		myturtle.forward(length)
		myturtle.right(angle)

def row(myturtle,numshapes):
	for i in range(3):
		shape(joe,50,4,90)
		joe.penup()
		joe.right(90)
		joe.forward(50)
		joe.left(90)
		joe.pendown()
def getRGB(): 
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return (r,g,b)
#main code
joe = turtle.Turtle()
joe.left(90)
turtle.colormode(255)
for i in range(3):
	row(joe,3)
	joe.penup()
	joe.left(90)
	joe.forward(3*50)
	joe.right(90)
	joe.forward(50)
	joe.pendown()

turtle.done() 

