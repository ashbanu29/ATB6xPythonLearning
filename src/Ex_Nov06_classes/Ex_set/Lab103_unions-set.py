a = {1,2,3,4,5}
b = {4,5,6,7}
print(a.union(b)) # this will print all the values and common elements ae print once.
print(a|b)

print(a.intersection(b)) # this will print only the common value from both the sets

print(a-b)
print(a.difference(b))
print(a-b)
print(b-a)
print(a.symmetric_difference(b)) # this will remove the common and print the other elements
print(a^b)
print("----------------")
set1 = {1,2,3,4}
set2 = {4,5,6}
print(set1.union(set2))

my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2)
print(my_set)
