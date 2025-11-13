from traceback import print_tb

cities = ("Berlin", "London", "Paris")
print(len(cities))

print("Paris" in cities)

cities.count("Paris")
cities.count("Berlin")
cities.count("London")
print(cities.count("Berlin"))

print("-------------------")
#user_input = input("Enter a city name: ")
for city in cities:
   print(city)


print("-------------------")

num = (1,2) * 3
print(num)

print(num.index(2))

my_list = [1,2,3,4,5]
my_tuple = tuple(my_list)
print(my_tuple)

print(my_list[0:4])
my_list = tuple([1,2,3,4,5])
print(my_tuple)

back_to_list=list(my_tuple)
print(back_to_list)

