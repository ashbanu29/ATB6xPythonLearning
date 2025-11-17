result =["pass", "FAIL", "PASS", "PASS"]

pass_give = list(filter(lambda x: x == "PASS", result))
print(pass_give)