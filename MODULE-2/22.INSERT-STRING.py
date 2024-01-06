def insert_in_middle(original_str, to_insert):
    middle_index = len(original_str) // 2
    result_str = f"{original_str[:middle_index]}{to_insert}{original_str[middle_index:]}"
    return result_str

# Example usage
user_input = input("Enter the original string: ")
string_to_insert = input("Enter the string to insert: ")

result = insert_in_middle(user_input, string_to_insert)

print("Result:", result)
