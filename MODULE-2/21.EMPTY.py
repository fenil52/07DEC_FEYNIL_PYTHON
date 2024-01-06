def create_new_string(input_str):
    # Check if the length is less than 2
    if len(input_str) < 2:
        return ""
    
    new_str = input_str[:2] + input_str[-2:]
    return new_str


user_input = input("Enter a string: ")
result = create_new_string(user_input)

print("Result:", result)
