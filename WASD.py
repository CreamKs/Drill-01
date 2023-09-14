import turtle

def Move_Up():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def Move_Left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
def Move_Right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)
def Move_Down():
    turtle.stamp()
    turtle.setheading(-90)
    turtle.forward(50)
    
turtle.shape('turtle')

turtle.onkey(Move_Up, 'w')
turtle.onkey(Move_Left, 'a')
turtle.onkey(Move_Right, 'd')
turtle.onkey(Move_Down, 's')
turtle.onkey(turtle.reset, 'Escape')
turtle.listen()
