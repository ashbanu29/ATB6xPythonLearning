numbers = {1,2,3,4,5,6,7,8,9,10}

def square(x):
    return x ** 2

sq_all_numbers = list(map(square, numbers))
print(sq_all_numbers)