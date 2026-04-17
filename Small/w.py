import turtle


def draw_small_w():
    screen = turtle.Screen()
    screen.title("Small w with Turtle")

    pen = turtle.Turtle()
    pen.speed(4)
    pen.pensize(3)

    # Start near the top-left of the letter.
    pen.penup()
    pen.goto(-60, 50)
    pen.pendown()

    # Down-up-down-up strokes to form lowercase 'w'.
    pen.goto(-30, -20)
    pen.goto(0, 50)
    pen.goto(30, -20)
    pen.goto(60, 50)

    pen.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    draw_small_w()
