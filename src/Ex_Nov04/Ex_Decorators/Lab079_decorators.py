def add_security(func):

    def wrapper():
        print("1.Before calling the function")
        print("2.Add helmet, License, gloves,RC")
        func()
        print("3.After calling the function")
        print("4.Secure driving")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("I am driving ola scooter")


@add_security
def drive_ubers():
    print("I am driving ubercar")
