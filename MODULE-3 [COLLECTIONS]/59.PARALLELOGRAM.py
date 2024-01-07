def parallelogram_area(base, height):
    area = base * height
    return area

# Example usage
base_length = float(input("Enter the length of the base: "))
height = float(input("Enter the height: "))

area = parallelogram_area(base_length, height)
print(f"The area of the parallelogram is: {area}")
