import turtle 

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 0)
t.setheading(90)   # face left
t.pendown()
t.forward(75)
t.backward(70)
t.forward(60)
t.left(90)
t.forward(30)
t.backward(30)
t.right(180)
t.forward(30)



turtle.done()