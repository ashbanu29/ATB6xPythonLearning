
# Inheritance concept

class BaseTest:

    def setup(self):
        print("base setup with browser and environment")

class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print("Running the test case")

#this will call both the fucntions this is called single inheritance
t = LoginTest()
t.run()

