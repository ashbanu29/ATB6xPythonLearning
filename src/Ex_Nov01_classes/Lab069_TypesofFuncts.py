#built in function

result = max(2,3)
print(result)

print("================")
#1. No return type and no argument/param

def greet():
    print("Hello")

greet()

print("================")

#2. No return type and with argument /parameter
def greet(name):
    print("Hello, " + name)

greet("Ayesha")

print("================")
#3. No return type with default argument

def say_hello_default(name="Ayesha"):
    print("Hello, " + name)

say_hello_default("Ayesha")
say_hello_default()


def mult_argument(name1 = "A", name2 = "B"):
    print("Mul ->" , name1, name2)

mult_argument(name1 = "A", name2 = "B")
mult_argument(name1 = "anu", name2 = "banu")

print("================")

#4. argument with return type

def sum(a, b):
    return a + b

print(sum(3, 4))
result = sum(3, 4)
print(result)


print("================")

def sum_of_num(n1=100, n2=200):
    return n1 + n2

result = sum_of_num(100, 200)
print(result)

result = sum_of_num(50, 200)
print(result)

result = sum_of_num()
print(result)
