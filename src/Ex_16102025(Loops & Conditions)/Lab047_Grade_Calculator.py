"""
write a program to calculate the grades in the form of Letter Score (A,B,C,D,E,F)
A - 90-100
B - 80-89
C - 70-79
D - 60-59
F - 0-49
"""

score = int(input("Enter the score: ").strip())

if score >= 100 or score <= 0:
    print("Enter the valid score", score)
else:
    if score >=90 and score <= 100:
        print("The Grade is: A", score)
    elif score >= 80 and score <= 89:
        print("The Grade is: B", score)
    elif score >= 70 and score <= 79:
        print("The Grade is: C", score)
    elif score >= 60 and score <= 59:
        print("The Grade is: D", score)
    else:
        print("The Grade is: F", score)


