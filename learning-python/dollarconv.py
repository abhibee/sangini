# def dollar2rupee(dollar):
# 	return dollar*70
# dollar=5
# print dollar2rupee(dollar), "Rs is the value of $", dollar
def rupee2dollar(rupee):
    return rupee / 70.0
rupee = input("enter rupees :")
print(rupee2dollar(float(rupee)), "dollar is the value of Rs", rupee)
