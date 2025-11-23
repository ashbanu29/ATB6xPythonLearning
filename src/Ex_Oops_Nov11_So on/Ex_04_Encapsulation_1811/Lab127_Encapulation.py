class Car:

    make = None
    year = None
    model = None

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Car is starting... with make", self.make)
        print("Car is starting... with model", self.model)
        print("Car is starting... with year", self.year)

lambo = Car("Ford", "Mustang", 1999)
lambo.start_engine()
