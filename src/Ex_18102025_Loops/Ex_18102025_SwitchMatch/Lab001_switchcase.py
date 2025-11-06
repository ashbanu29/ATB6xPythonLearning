from unittest import case

day = int(input("Enter the day: "))
match day:
    case 1:
        print("The day is Monday")
    case 2:
        print("The day is Tuesday")
    case 3:
        print("The day is Wednesday")
    case 4:
        print("The day is Thursday")
    case 5:
        print("The day is Friday")
    case 6:
        print("The day is Saturday")
    case 7:
        print("The day is Sunday")
    case _:
        print("The day is Invalid")