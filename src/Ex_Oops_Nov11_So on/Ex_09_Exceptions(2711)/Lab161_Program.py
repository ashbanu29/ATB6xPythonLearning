
a = int(input("enter a number"))
b = int(input("enter b number"))

try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("division by zero is not possible")
