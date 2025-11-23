#Inheitance means : acquiring the properties of parent class to child class

class BaseTest:
    driver = "chrome"
    def setup(self):
        print("base class setup with the browser environment")


class HomeTest(BaseTest):
    def run(self):
        self.setup()
        print("home test running", self.driver) # the driver variable is inherited from parent class


t = HomeTest()
t.run()
