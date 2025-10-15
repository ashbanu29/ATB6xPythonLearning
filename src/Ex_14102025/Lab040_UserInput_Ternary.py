user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("User is allowed to vote")
else:
    print("User is not allowed to vote")
print(user_age)

print("User is allowed to vote" if user_age >= 18 else "User is not allowed to vote")

