import turtle

t = turtle.Pen()
# turtle.Screen().bgcolor("black")
t.getscreen().bgcolor("black")
t.speed(0)
sides = 6
colours = ['red','yellow','blue','green','orange','purple']
for x in range(360):
    t.pencolor(colours[x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 91)
    t.width(x*sides/200)



t.getscreen().getcanvas().postscript(file="spiral.ps", colormode='color')