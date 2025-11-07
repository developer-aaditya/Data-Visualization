print("Enter sides for the triangle : ")
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

def is_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print("The triangle is valid")

    if side1 == side2 == side3:
        print("It is an equilateral triangle")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("It is a isosceles triangle")
    else:
        print("It is not a isosceles triangle")

is_triangle(side1, side2, side3)