#program to check the year is a leap year or not

def check_lapyear(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = 2024
result = check_lapyear(year)
print(result)