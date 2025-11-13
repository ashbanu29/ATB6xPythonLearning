import math

num = int(input("enter a number"))

l_num = lambda num: math.floor(num/2)
print(l_num(num))

op = lambda : math.pow(int(input("enter a number")), 2)
print(op())