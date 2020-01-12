
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange",
        "purple", "white", "brown", "gray", "pink",'tan','coral','brown',
          'coral','navy','violet']
family = []
name = turtle.textinput("My family",
                      "Enter a name, or just hit [ENTER] to end:")
while name != "":
    family.append(name)
    name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
for x in range(100):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)], font = ("Arial", ((x+4)//4), "bold") )
    t.left(360/len(family) + 3)
