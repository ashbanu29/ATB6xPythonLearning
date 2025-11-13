from operator import index

#pop() - will delete the last index bydefault or else, it will delete based on the indexation
squares = [1, 4, 6, 8]
print(squares)
print(squares.pop())
print(squares)

squares.pop(1)  # 4 will be deleted because at index 1 4 is available
print(squares)

# clear() this will clear the list
squares.clear()
print(squares)

numbers = [1, 2, 3, 4, 5, 4,4]
print(numbers.index(3))

# count() - this will count of number of indexes or elements exists in the list
print(numbers.count(4))

#sort
numbers.sort(reverse=True)
print(numbers)

#reverse() - will reverse the list of items
numbers.reverse()
print(numbers)

#max(), min(), sum()
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(numbers)
print("-------------")
#slicing
print(min(numbers))
print(numbers[1:4]) # 4 means n-1 that means 4-1 =3rd index value will be displayed
print(numbers[-1]) # last element
print("apple" in numbers)
print(2 in numbers)

print("-------------")
# list creation and comprehension

l = list(range(1,5))
print(l)

print("-------------")

#list of list or Nested list concept
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1])


#delete is a keyword, remove() is a function
#clear will clear everything, pop will return delete will not return
del numbers[1]
print(numbers)




