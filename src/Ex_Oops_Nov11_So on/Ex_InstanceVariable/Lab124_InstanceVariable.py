a = 10 # variable which is available evrywhere in the program

class Person:
    b = 11 # this is called instance variable vch is only available within the class

    def print_info(self):
        c = 10  # local variable, this exist within the method or function
        print(c) # this can directly called or access directly
        print(self.b) #b can be accessed by using self keyword because this is class variable
        print(a) # this can be used anywhere outside or inside the class because this can be used anywhere


obj_ref = Person()
obj_ref.print_info()
obj_ref.print_info()