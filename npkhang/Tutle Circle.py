import turtle

myTurtle = turtle.Turtle()
myTurtle.circle(50)
for d in range(0, 100):
    d=d+1
    myTurtle.penup()
    myTurtle.setposition(d+10,d-10)
    myTurtle.pendown()
    myTurtle.circle(50)
     
turtle.getscreen()._root.mainloop()
