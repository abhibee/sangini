name = input('what is your name')
while name != " ":
    for x in range(100):
        print(name,end="  ")
        print()
    name = input('type another name, or just hit [enter] to quit ')
print('thanks for playing')