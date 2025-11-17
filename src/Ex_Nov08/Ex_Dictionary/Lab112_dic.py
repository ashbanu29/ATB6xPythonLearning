dic1 = {"a" : 1, "b" : 2, "c" : 3}
print(dic1.keys())
print(dic1.values())

dict2 = {"a" : 1, "b" : 2}
print(dict2.keys())
print(dict2.values())

missing_keys = set(dic1.keys() - dict2.keys())
print(missing_keys)
