"""
Write a program to calculate the area of circle given its radius using the formula
area = pi * r^2 (Take pie as 3.14)
"""
import math

pi = 3.14987654
radius = float(input("Enter the radius of the circle:\n "))
print(radius)

#area = 3.14987654 * pow(radius, 2)
area = math.pi * radius ** 2
print("area of the circle is: ", area)
print(f"Area of the circle is: {area: .2f}")
