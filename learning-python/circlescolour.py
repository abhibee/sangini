import turtle
t = turtle.Pen()
colours = ["red", "yellow", "blue", "green","orange", "purple", "white", "gray",'pink','light blue','brown', 'light green']
t.speed(20)
for x in range(12):
    t.fillcolor(colours[x % colours.__sizeof__()])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.left(30)
turtle.textinput("Enter your name", "Done")