

class Bank:

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.balance = balance


    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount


    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def show_account(self, is_auth):
        if is_auth:
            print("Account Number: ", self.__account_number)
        else:
            print("Not allowed")

SBI_bank = Bank(1213123223, 100)
SBI_bank.deposit(100)
SBI_bank.check_balance()
SBI_bank.show_account(True)
print()