class Cal:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display_sum(self):
        return self.a + self.b

    def display_sub(self):
        return self.a - self.b


obj_ref = Cal(2,3)
print(obj_ref.display_sum())
print(obj_ref.display_sub())
print(obj_ref.display_sum())