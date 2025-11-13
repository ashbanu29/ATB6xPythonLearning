import time

def print_logs(func):

    def wrapper():
        print("start of the log")
        func()
        print("end of the log")
    return wrapper

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("start of the time")
        func()
        end_time = time.time()
        print("end of the time")
        print("Total time taken by function is: ", end_time - start_time)

    return wrapper

@time_decorator
@print_logs
def user_UI_test():
    print("Time taken by this function1")
    time.sleep(2)

@time_decorator
@print_logs
def user_UI_test2():
    print("Time taken by this function2")
    time.sleep(5)

user_UI_test2()
user_UI_test()