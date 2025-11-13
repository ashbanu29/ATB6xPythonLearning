def start_code(func):
    print("1.Before running the code")
    print("Start the browser")


def end_code(func):
    print("After running the Test case")
    print("End the browser")

def user_UI_test():
    print("User UI test")

start_code(user_UI_test)
user_UI_test()
end_code(user_UI_test)