def decorato1(func):
    def wrapper():
        print("decorato1")
        func()
    return wrapper

def decorato2(func):
    def wrapper():
        print("decorato2")
        func()

    return wrapper

@decorato1
@decorato2
def say_hello():
    print("Hello World")


say_hello()
