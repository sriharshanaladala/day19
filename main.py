from turtle import Turtle, Screen

tm = Turtle()
screen = Screen()


def move_forward():
    tm.forward(10)


def move_backward():
    tm.backward(10)


def move_left():
    tm.left(10)


def move_right():
    tm.right(10)


def clear():
    tm.clear()
    tm.penup()
    tm.home()
    tm.pendown()


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(clear, "c")
screen.exitonclick()
