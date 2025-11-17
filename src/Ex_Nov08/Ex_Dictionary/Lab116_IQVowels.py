#what is the ovals in the given string

input_string = "hello world"
vowals = "aeiou"

vowals_count = 0
result = list()

for char in input_string:
    if char in vowals:
        vowals_count += 1
        result.append(char)
print(vowals_count)
print(result)
