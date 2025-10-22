#take the 3 inputs and find the maximum number

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
num3 = int(input("Enter a number3: "))

if num1>=num2 and num1>=num3:
    print("The Maximum is:", num1)
elif num2>=num3 and num2>=num1:
    print("The Maximum is:", num2)
else:
    print("The Maximum is:", num3)
