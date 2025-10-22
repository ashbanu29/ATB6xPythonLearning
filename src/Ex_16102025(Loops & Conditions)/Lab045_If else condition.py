#check for the maximum value

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter another number2: "))

if num1>=num2:
    print("Maximum is:", num1)
elif num2>=num1:
    print("Maximum is:", num2)
else:
    print('Not equal to or greater than or equal to:', num1)