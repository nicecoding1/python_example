"""
b – moves the turtle backward 1 unit
d – places the turtle's pen down
f – moves the turtle forward 1 unit
l – turns the turtle to the left by 1 degree
r – turns the turtle to the right by 1 degree
u – raises the turtle's pen up
x – exits the Picologo program

program run: spy3 as2.py < testfile.pico
"""

import turtle
import sys


def draw(n, c):
    for i in range(1, n+1):
        if c == 'b':
            turtle.back(1)
        elif c == 'd':
            turtle.pendown()
        elif c == 'f':
            turtle.forward(1)
        elif c == 'l':
            turtle.left(1)
        elif c == 'r':
            turtle.right(1)
        elif c == 'u':
            turtle.penup()


cmd = ['b', 'd', 'f', 'l', 'r', 'u', 'x']
p = []
tmp = sys.stdin.readlines()

for i in tmp:
    p.append(i.strip("\n"))

num = 1
line = 0
err = 0
for i in p:
    line = line + 1
    if len(i)>1:
        print("*** command too long at line", line)
        err = err + 1
    elif i == "":
        pass
    elif i.isdigit():
        num = num * int(i)
    else:
        if i not in cmd:
            print("*** unknown command at line", line)
            err = err + 1
            continue
        if i == 'x':
            break
        else:
            draw(num, i)
            num = 1

if err > 0:
    print("*** there were %s errors" % str(err))

