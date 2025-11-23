
# Multiple Inheritance concept

class APIBase:

    def api_auth(self):
        print("Authentication --> api_auth")


class DBBase:

    def db_connect(self):
        print("Conneting to the Database")

class TestHybridAPI(APIBase, DBBase):
    def run(self):
        self.api_auth()
        self.db_connect()
        print("Testing Hybrid API")

# both the classes has called because of multiple Inheritance
tc1 = TestHybridAPI()
tc1.run()