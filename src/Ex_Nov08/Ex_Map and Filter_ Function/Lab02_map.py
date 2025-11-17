name = ["ashu", "junnu", "sannu"]

def upper_case(string):
    return string.upper()

n = upper_case("anisha")
print(n)


name = list(map(upper_case, name))
print(name)     