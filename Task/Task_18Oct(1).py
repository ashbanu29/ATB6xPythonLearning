"""
Question 1. :Given a Number a number you need to calculate the factorial of that number
n = 5
Fact = 5×4×3*2*1 = 120
Fact = 0 → 1,

n = int(input("Enter the number:"))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print("The factorial of",n,"is",factorial)
"""


num = int(input("Enter the number:"))

factorial = 1

if num < 0:
    print("Factorial is not defined")
if num == 0:
    print("Factorial is 1", factorial)
else:
    for i in range(1,num+1):
        factorial *= i
print("The factorial of",num,"is",factorial)
