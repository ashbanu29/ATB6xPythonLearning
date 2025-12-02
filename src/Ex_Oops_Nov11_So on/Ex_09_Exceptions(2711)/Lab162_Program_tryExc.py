a = int(input("enter a number"))
b = int(input("enter b number"))

try:
    c = a / b
    print(c)
except (ZeroDivisionError, TypeError, ValueError, NameError):
    print("division by zero is not possible")