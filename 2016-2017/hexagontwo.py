import turtle
joe = turtle.Turtle()
joe.color("red")
joe.left(90)

def square(joe):
   joe.begin_fill() 
   for i in range(6):
	joe.forward(50)
     	joe.left(60)
   joe.end_fill()


square(joe)
for i in range(4):  
   square(joe)   
   joe.right(90)
   joe.forward(50*1.75)
   joe.left(90)
turtle.done()

