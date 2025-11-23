from enum import nonmember

print("outside the class")

class MobilePhone:

    model = None

    def __init__(self): #constructor
        print("DC")

    def talk(self):
        print("Hi talking")

iphone = MobilePhone()
iphone.talk()
print("outside the class")
