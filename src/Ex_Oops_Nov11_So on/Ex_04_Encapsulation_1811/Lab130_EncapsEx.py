
class Car:


    def __init__(self):
        self.password = "abc"
        self.__password = "pass123" # private variable cannot be access outside the method

    def login(self):
        self.password = input("Enter Password: ")
        self.__password = "123PAAS" # onlyu login can access the password which is secured and encapsulated

obj_ref = Car()
obj_ref.login() # private variable can be access only via the method
print(obj_ref.password)
