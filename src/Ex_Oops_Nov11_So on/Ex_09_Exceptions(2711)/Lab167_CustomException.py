
class InvalidAgeError(Exception):
    pass

def check_zero(a):
    if a < 0:
        raise ZeroDivisionError("cannot divide by zero")


def can_you_drink(age):
    if age < 18:
        raise InvalidAgeError("You can't drink.")
    else:
        print("You can drink.")
can_you_drink(19)