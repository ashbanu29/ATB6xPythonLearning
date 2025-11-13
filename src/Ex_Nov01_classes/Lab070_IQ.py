#programt to enter the numbers from users and sum it, if the user has not given any number take
# the default numbers

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))


def sum_of_num(n1=10,n2=20,n3=30):
    return n1 + n2 + n3

result = sum_of_num(1,2,3)
print(result)

result1 = sum_of_num()
print(result1)