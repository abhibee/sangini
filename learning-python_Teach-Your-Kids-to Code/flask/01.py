
def tellmore(name, gender):
    print(name, "is a good", 'boy' if (gender == "m") else'girl')


name = input("whats your name")
gender = input("whats your gender (m/f)")
tellmore(name, gender)
