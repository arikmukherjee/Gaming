import turtle


def draw_small_u():
    screen = turtle.Screen()
    screen.title("Small u with Turtle")

    pen = turtle.Turtle()
    pen.speed(4)
    pen.pensize(3)

    # Start near the top-left of the letter.
    pen.penup()
    pen.goto(-40, 50)
    pen.pendown()

    # Left vertical stroke down.
    pen.setheading(-90)
    pen.forward(60)

    # Bottom curve.
    pen.circle(20, 180)

    # Right vertical stroke up.
    pen.forward(60)

    pen.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    draw_small_u()
