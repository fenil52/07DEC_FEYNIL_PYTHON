def revers(input_str):
    if len(input_str) % 4 == 0:
        reversed_str = input_str[::-1]
        return reversed_str
    else:
        return input_str

# Example usage
user_input = input("Enter a string: ")
result = revers(user_input)

print("Result:", result)
