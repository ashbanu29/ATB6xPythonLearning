my_dic = {
    "key1": "value1",
    "key2": "value2",
}

print(my_dic)
my_dic["key3"] = "value3"
print(my_dic["key3"])

my_dic["key4"] = "TestEngineer"
print(my_dic)

del my_dic["key4"]
print(my_dic)

for key, value in my_dic.items():
    print(key, value)
