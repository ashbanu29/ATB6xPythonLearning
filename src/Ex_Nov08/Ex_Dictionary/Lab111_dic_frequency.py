#count the frquency or count the number of each word in the gien string


string = "Testing QA"

string = input("Enter the string to count the characters")
count = {}
for char in string:
    count[char] = count.get(char, 0) + 1

print(count)