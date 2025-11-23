

class Home:

    def __init__(self):
        self.public_var = "father"
        self.__private_var = "baby"

    def mom(self):
        print(self.__private_var)
        self.__wife

    def __wife(self):
        print("Private wife")


obj_ref = Home()
obj_ref.mom()