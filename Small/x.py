import turtle


def draw_small_x():
    screen = turtle.Screen()
    screen.title("Small x with Turtle")

    pen = turtle.Turtle()
    pen.speed(4)
    pen.pensize(3)

    # First diagonal stroke.
    pen.penup()
    pen.goto(-40, 50)
    pen.pendown()
    pen.goto(40, -20)

    # Second diagonal stroke.
    pen.penup()
    pen.goto(40, 50)
    pen.pendown()
    pen.goto(-40, -20)

    pen.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    draw_small_x()
