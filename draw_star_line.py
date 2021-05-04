import turtle
import random

screen = turtle.Screen()
screen.screensize(500, 500)
t = turtle.Turtle()
t.shape("turtle")


def getrgb():
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


def star(length):
    r, g, b = getrgb()
    t.pendown()
    t.begin_fill()
    t.color(r, g, b)

    for i in range(5):
        t.forward(length)
        t.right(144)

    t.end_fill()
    t.penup()


def drawline(x, y):
    t.pendown()
    t.goto(x, y)

s = turtle.textinput("입력", "별의 개수를 입력하시오: ")
num = int(s)

for n in range(num):
    x = random.randrange(-300, 300)
    y = random.randrange(-300, 300)

    t.up()
    t.goto(x,y)
    t.down()

    star(random.randint(100, 200))

t.screen.onclick(drawline)

turtle.mainloop()
