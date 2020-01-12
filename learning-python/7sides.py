

import turtle

t = turtle.Turtle()
t.speed(0)
t.width(4)

colors = ["red", "orange", "yellow",
          "green", "blue", "violet"]

for x in range(200):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(360/6)
