# RosetteGoneWild.py
import turtle
t = turtle.Pen()
t.getscreen().bgcolor("black")
t.speed(-1234567890)
t.width(3)

number_of_circles = int(turtle.numinput("Number of circles",
                                        "How many circles in your rosette?", 6))
for x in range(number_of_circles):
    t.pencolor('red')
    t.circle(100)
    t.left(360/number_of_circles)
    t.pencolor('yellow')
    t.circle(50)
turtle.textinput("Enter your name", "Done")
t.getscreen().getcanvas().postscript(file="spiral.ps", colormode='color')