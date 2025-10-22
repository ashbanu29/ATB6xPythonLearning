# Find the positive number is even or odd

num = int(input("Enter a number: ").strip())

if num>0:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Not even")

if num>0:
    print("Even" if num % 2 == 0 else "Odd")
else:
    print("Negative number")