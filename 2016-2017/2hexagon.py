import turtle
fill(true):
   color("red")
joe = turtle.Turtle()
def hexagon(joe):
   joe.forward(50)
   joe.left(60)
for i in range(8):
   hexagon(joe)
fill(false):
turtle.done()
