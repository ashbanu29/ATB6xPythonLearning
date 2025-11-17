square = {x ** 2 for x in range(5)}
print(square)

for x in range(5):
    square.add(x**2)
print(square)

#Frozen set is cannot be change just like tuple

fset = frozenset([1,23])
print(fset)

fset.add(2)