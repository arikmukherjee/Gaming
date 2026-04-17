import turtle


def draw_small_v():
    screen = turtle.Screen()
    screen.title("Small v with Turtle")

    pen = turtle.Turtle()
    pen.speed(4)
    pen.pensize(3)

    # Start near the top-left of the letter.
    pen.penup()
    pen.goto(-40, 50)
    pen.pendown()

    # Downward diagonal to the bottom point.
    pen.goto(0, -20)

    # Upward diagonal to the top-right.
    pen.goto(40, 50)

    pen.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    draw_small_v()
