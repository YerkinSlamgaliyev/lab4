import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("Enter angle in degrees: "))
radian = degree_to_radian(degree)
print(f"{degree} degrees is {radian} radians.")

def area_of_trapezoid(base1, base2, height):
    return ((base1 + base2) / 2) * height

base1 = float(input("Enter the length of the first base of the trapezoid: "))
base2 = float(input("Enter the length of the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
trapezoid_area = area_of_trapezoid(base1, base2, height)
print(f"The area of the trapezoid is: {trapezoid_area}")

def area_of_regular_polygon(sides, length):
    return (sides * length**2) / (4 * math.tan(math.pi / sides))

sides = int(input("Enter the number of sides of the regular polygon: "))
length = float(input("Enter the length of one side of the polygon: "))
polygon_area = area_of_regular_polygon(sides, length)
print(f"The area of the regular polygon is: {polygon_area}")

def area_of_parallelogram(base, height):
    return base * height

base = float(input("Enter the base length of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))
parallelogram_area = area_of_parallelogram(base, height)
print(f"The area of the parallelogram is: {parallelogram_area}")
