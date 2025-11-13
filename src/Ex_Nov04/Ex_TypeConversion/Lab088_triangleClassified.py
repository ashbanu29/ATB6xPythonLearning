side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))

def triangle():# Check if the input can form a valid triangle
    return side1, side2, side3

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 > 0 and side2 > 0 and side3 > 0:
    # Check for triangle type
        if side1 == side2 == side3:
            print("This is an Equilateral triangle.")
        elif side1 == side2 or side2 == side3 or side1 == side3:
            print("This is an Isosceles triangle.")
        else:
            print("This is a Scalene triangle.")
    else:
        print("The given sides do not form a valid triangle.")

print(triangle())
