num = [1,2,3,4,5,6,7,8,9]
print(num)

def odd_num(num):
    return num % 2 != 0


print_odd_num = list(filter(odd_num, num))
print(print_odd_num)