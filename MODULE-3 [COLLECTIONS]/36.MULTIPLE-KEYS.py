# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Keys to check
keys_to_check = ['a', 'c','b']

# Check if all keys exist in the dictionary
all_keys_exist = all(key in my_dict for key in keys_to_check)

# Print the result
if all_keys_exist:
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
