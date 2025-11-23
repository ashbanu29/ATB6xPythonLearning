import email


class Wellableapp:


    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "rahul.tomar@embitel.com" and self.password == "Password@123":
            print("Login Successful")
        else:
            print("Login Failed")

email = input("Enter Email: ")
password = input("Enter Password: ")
app = Wellableapp(email, password)
app.login_confirm()

