#Print even numbers between 1 and 20
for i in range(1,20):
    if i%2 == 0:
        print(i, "The number is even")

    else:
        pass

print("----------")

#Skip numbers divisible by 3, from (0,100)

for i in range(0,100):
    if i%3 == 0:
        continue
    else:
        print(i)

print ("===============")
#Print numbers from 10 down to 1

for i in range(10, 0, -1):
    print(i)