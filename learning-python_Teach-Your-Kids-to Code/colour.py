import turtle
t = turtle.Pen()
# turtle.Screen().bgcolor("black")
t.getscreen().bgcolor("black")
t.speed(0)
colours = ['red','yellow','blue','green']
for x in range(200):
    t.pencolor( colours[ x % 4])
    t.forward(x)
    t.left(90)
# t.getscreen().getcanvas().postscript(file="file_name.ps", colormode='color')