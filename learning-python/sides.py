import turtle

t = turtle.Pen()
t.getscreen().bgcolor("black")
t.speed(0)
sides = eval(input('Enter a number of sides between 2-6:'))
colours = ['red','yellow','blue','green','orange','grey','pink','light blue','white','purple']
for x in range(160):
    t.pencolor(colours[x%sides])
    t.pencolor( colours[ x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/100)
