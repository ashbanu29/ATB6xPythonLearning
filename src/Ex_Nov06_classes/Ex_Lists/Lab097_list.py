import copy

my_list = [1, 2, 3,7]
print(my_list[0])

my_list[1] = 4
my_list[2] = "ayesha"
my_list[3] = "banu"

print(my_list)


for item in my_list:
    print(item)

print("element : ", my_list[0])
print("element : ", my_list[1])
print("element : ", my_list[2])

print("----------")
#append() (add the 1 element at the end of the list)
my_list.append("hello")
print(my_list)

#extend() will add the new list to the existing list.
# like this [1, 4, 'ayesha', 'banu', 'hello', 6, 7, 8, 9, 10]
my_list.extend([6,7,8,9,10])
print(my_list)

#by using this my_list[0]=0, the index value we can change the value of that particular index.
my_list[0] = 0
print(my_list)

#insert will add the element to the existing list on particular index and move/shift the elements
#to right side

my_list.insert(1,"Hi")
print(my_list)

#remove()
my_list.remove("Hi") # hi is removed from the list.
print(my_list)

# .copy() - will copy the entire list

print("=====================")
copy_list = my_list.copy()
print(copy_list)
print("=====================")

#.reverse() - This will reverse the entire list.
copy_list.reverse()
print(copy_list)
print("=====================")

copy_list.remove(6)
print(copy_list)

copy_list.reverse()
print(copy_list)
print(my_list)

