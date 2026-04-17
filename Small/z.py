import turtle


def draw_small_z():
    screen = turtle.Screen()
    screen.title("Small z with Turtle")

    pen = turtle.Turtle()
    pen.speed(4)
    pen.pensize(3)

    # Start at top-left.
    pen.penup()
    pen.goto(-40, 50)
    pen.pendown()

    # Top horizontal stroke.
    pen.goto(40, 50)

    # Diagonal down-left stroke.
    pen.goto(-40, -20)

    # Bottom horizontal stroke.
    pen.goto(40, -20)

    pen.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    draw_small_z()
