class Person:

    def __init__(self):
        print("Lets take the user inputr")
        self.name = input("What is your name? ")
        self.age = input("What is your age? ")
        self.phone = input("What is your phone number? ")
        self.occupation = input("What is your occupation? ")


    def display_values(self):
        print("Name is :", self.name, "AGe is :", self.age, "Phone number is :", self.phone, "Occupation is: ", self.occupation)

persona_name = Person()
persona_name.display_values()
persona_phone = Person()