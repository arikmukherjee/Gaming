import turtle


def draw_small_y():
    screen = turtle.Screen()
    screen.title("Small y with Turtle")

    pen = turtle.Turtle()
    pen.speed(4)
    pen.pensize(3)

    # Left branch down to the center.
    pen.penup()
    pen.goto(-40, 50)
    pen.pendown()
    pen.goto(0, 10)

    # Right branch to the center.
    pen.penup()
    pen.goto(40, 50)
    pen.pendown()
    pen.goto(0, 10)

    # Descender stroke.
    pen.goto(0, -50)

    pen.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    draw_small_y()
