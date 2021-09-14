import turtle

def movew():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def movea():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def moves():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def moved():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()


turtle.shape('turtle')

turtle.onkey(movew,'w')
turtle.onkey(movea,'a')
turtle.onkey(moves,'s')
turtle.onkey(moved,'d')
turtle.listen()
