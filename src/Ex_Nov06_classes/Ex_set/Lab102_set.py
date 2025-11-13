#set() - Collection of unique elements and immutable which cannot be changed
#recognized by parenthesis
from traceback import print_tb

set_elements = {1,2,3,4,5}
print(set_elements)

list_set = list(set_elements) #converting from set to list
print(list_set)

set1 = set(list_set) # conversion from list to set
print(set1)

mixed = {1,"QA",3,4.6,5}
print(mixed)

empty = set()
print(type(empty))

for item in mixed:
    print(item)

mixed.add(10)
print(mixed)
#set is an unordered list which does not follow any kind of sequence
item = {"Ayesha", 2, 3, True, False, 5.6}
print(item)


for i in range(1,5):
    if i == 1:
        print("*")
    else:
        print("*" *i)
