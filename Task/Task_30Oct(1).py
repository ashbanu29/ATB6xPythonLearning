"""Q - Create a function which will take a positive number from the user and perform square
of the number?
i/o = 3
o/p = 9
"""
num = int(input("Enter a positive number: "))

def square(num):
    return num ** 2

print("The square of the number is ", square(num))