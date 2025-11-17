# remove duplicates


my_dict = {"a": 20, "b": 10, "c": 40, "d": 40}
print(my_dict)

unique_value = set()
result = {}

for key, value in my_dict.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)

print(result)