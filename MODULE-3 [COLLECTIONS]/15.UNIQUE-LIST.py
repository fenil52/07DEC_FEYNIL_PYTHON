def get_unique_values(input_list):
    unique_values = list(set(input_list))
    return unique_values

# Example usage:
original_list = [1, 2, 3, 2, 1, 4, 5]
result = get_unique_values(original_list)

print("Original List:", original_list)
print("Unique Values:", result)
