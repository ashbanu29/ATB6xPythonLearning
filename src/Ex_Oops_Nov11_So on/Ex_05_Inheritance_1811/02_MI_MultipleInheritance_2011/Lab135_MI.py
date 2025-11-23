
class Father1:
    def money(self):
        print("F1 Money")


class Father2:
    def money(self):
        print("F2 Money")

class Child(Father1, Father2):
    def give_money(self):
        print("Child Money")
        self.money()

c = Child() #it will print the first class which ever is there during the extend like in line no 11
c.give_money()