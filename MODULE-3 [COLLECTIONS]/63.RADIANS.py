import math

def degrees_to_radians(degrees):
    radians = degrees * math.pi / 180
    return radians

# Example usage
degrees_input = float(input("Enter the angle in degrees: "))
radians_output = degrees_to_radians(degrees_input)

print(f"{degrees_input} degrees is equal to {radians_output} radians.")
