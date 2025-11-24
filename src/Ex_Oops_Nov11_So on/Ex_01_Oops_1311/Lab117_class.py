def walk(name):
    print("I can walk")
    print("I can walk", name)


class Person:
    #Attributes
    name = None
    age = None
    height = None
    weight = None
    gender = None


#Behavior

    def talk(self): # self will be first argument
        print("I can talk")


    def eat(self, name): # argument with no return type
        print("I can eat")
        print("I can eat", name)

    def walk_return(self):
        print("I can walk ")
        return "I can walk "


nitu = Person()
print(nitu.name())
nitu.walk("anisha")

