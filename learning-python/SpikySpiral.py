import turtle, colorsys
t=turtle.Pen()
t.speed(0)
t.hideturtle()
t.width(4)
for x in range(1000):
    t.color(colorsys.hsv_to_rgb(x/600, .99, .99))
    t.forward(x)
    t.left(198)
