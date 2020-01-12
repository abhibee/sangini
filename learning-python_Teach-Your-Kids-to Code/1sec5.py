answer = input('do you want to see a spiral? y/n:')
if answer == 'y':
    print('working...')
    import turtle
    t = turtle.Pen()
    t.speed(0)
    t.width(2)
    for x in range(100):
        t.pendown
        t.forward(x*2)
        t.left(89)
print('okay,we are done! ')
