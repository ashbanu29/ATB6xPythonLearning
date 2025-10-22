
# checking for the edge cases

age = int(input("Enter the age:").strip())
if age <= 0 or age >= 100:
    print("Enter the valid age \n")
else:
    if age >= 21:
        print("You are eligible to go to club")
    else:
        print("You are not eligible to go to club")
