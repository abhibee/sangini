
def runtraffic():
    colour = input('what colour is the signal?: ')
    if colour =='red':
        print('stop!')
    elif colour =='green' :
        print('go!')
    elif colour =='yellow' :
        print('wait!')
    else:
        print('not a valid signal. Program exiting')
        exit(0)
while (True) :
    runtraffic()