#ClickAndSmile.py
import random
import turtle


def draw_smiley(x,y):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    # Face
    pen.pencolor("yellow")
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()
    # Left eye
    pen.setpos(x-15, y+60)
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
    # Right eye
    pen.setpos(x+15, y+60)
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
    # Mouth
    pen.setpos(x-25, y+40)
    pen.pencolor("black")
    pen.width(10)
    pen.goto(x-10, y+20)
    pen.goto(x+10, y+20)
    pen.goto(x+25, y+40)
    pen.width(1)


pen = turtle.Pen()
pen.speed(0)
pen.hideturtle()
turtle.bgcolor("black")
turtle.onscreenclick(draw_smiley)
turtle.getscreen()._root.mainloop()

