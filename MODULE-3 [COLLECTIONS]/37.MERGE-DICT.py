# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dictionaries using the update() method
merged_dict = dict1.copy()  # Create a copy to avoid modifying the original dict1
merged_dict.update(dict2)

# Printing the result
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)
