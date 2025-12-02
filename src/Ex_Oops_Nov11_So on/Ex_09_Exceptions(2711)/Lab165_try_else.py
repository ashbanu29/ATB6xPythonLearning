try:

    a = int(input("enter a number"))
    b = int(input("enter b number"))

    c = a / b

except ZeroDivisionError:
    print("division by zero is not possible")
except TypeError:
    print("Type error")
except ValueError:
    print("Value error")

else: # if try is succeed then only it will raise and print
    print(c)
    print("no error")
finally:
    print("I will always print")
