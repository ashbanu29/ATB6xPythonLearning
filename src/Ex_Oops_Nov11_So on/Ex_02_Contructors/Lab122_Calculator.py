class Calculator:
    a = None
    b = None

    def __init__(self):
        print("Calculator")

    def sum(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))

s = Calculator()

sum = s.sum(a,b )
sub = s.sub(a, b)
mul = s.mul(a, b)

print("Sum is", sum)
print("Sub is: ", sub)
print("mul is ", mul)
