#t = open('testdata.txt', 'r')
#t = open('testdata.txt', 'w')
#t = open('testdata.txt', 'w+')
#t = open('testdata.txt', 'r+')

#t.close()

try:
    with open('testdata.txt', 'r') as file:
        data = file.readlines() # list manner

        print(data)
except FileNotFoundError as e:
    print(e)