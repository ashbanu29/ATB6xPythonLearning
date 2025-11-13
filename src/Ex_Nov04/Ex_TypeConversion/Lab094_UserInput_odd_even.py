
user = int(input("Enter a number: "))

check_even_odd = lambda num: "even" if num %2==0 else "odd"
print(check_even_odd(user))