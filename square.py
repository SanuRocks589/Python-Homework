import turtle 

turtle.Screen().bgcolor("turquoise")
turtle.Screen().setup(500,500)
vari = turtle.Turtle() 
side = 4
for i in range(side):
    vari.forward(50)
    vari.right(360/side)
turtle.done