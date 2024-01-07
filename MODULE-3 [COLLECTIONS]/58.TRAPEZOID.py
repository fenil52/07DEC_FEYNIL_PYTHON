def trapezoid_area(base1, base2, height):
    area = (base1 + base2) * height / 2
    return area

# Example usage
base1_length = float(input("Enter the length of the first base: "))
base2_length = float(input("Enter the length of the second base: "))
height = float(input("Enter the height: "))

area = trapezoid_area(base1_length, base2_length, height)
print(f"The area of the trapezoid is: {area}")
