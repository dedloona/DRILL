import turtle
count = 0
turtle.penup()
turtle.goto(-250,-250)
turtle.pendown()
while(count < 6):
	turtle.forward(500)
	turtle.penup()
	turtle.backward(500)
	turtle.left(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.pendown()
	count = count + 1
turtle.penup()
turtle.goto(-250,-250)
turtle.pendown()
count = 0
while(count < 6):
        turtle.left(90)
        turtle.forward(500)
        turtle.penup()
        turtle.backward(500)
        turtle.right(90)
        turtle.forward(100)
        turtle.pendown()
        count += 1
turtle.exitonclick
