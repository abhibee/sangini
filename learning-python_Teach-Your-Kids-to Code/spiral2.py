import turtle
t = turtle.Pen()
# turtle.Screen().bgcolor("black")
t.getscreen().bgcolor("black")
t.speed(0)
sides = 10
colours = ['red','yellow','blue','green','orange','grey','pink','light blue','white','purple']
for x in range(160):
    t.pencolor(colours[x%sides])
#    t.pencolor( colours[ x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/100)
t.getscreen().getcanvas().postscript(file="spiral.ps", colormode='color')