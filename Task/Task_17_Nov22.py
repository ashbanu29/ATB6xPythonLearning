#Create a framework base counter that counts test execution instances:

class BaseCounter:
    count = 0

    def __init__(self):
        BaseCounter.count += 1





count = BaseCounter()
count2= BaseCounter()
print(BaseCounter.count)