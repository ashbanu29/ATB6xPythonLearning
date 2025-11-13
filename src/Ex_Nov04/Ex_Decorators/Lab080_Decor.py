def before_after_UI(func):

    def wrapper():
        print("1.Before running UI code")
        func()
        print("2.After running UI code")

    return wrapper()

@before_after_UI
def test_UI():
    print("I am testing the UI code")