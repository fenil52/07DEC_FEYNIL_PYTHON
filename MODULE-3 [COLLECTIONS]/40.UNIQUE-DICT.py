# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1, 'f': 4}

# Create an empty set to store unique values
unique_values = set()

# Iterate through the values of the dictionary
for value in my_dict.values():
    unique_values.add(value)


print("Unique Values:", unique_values)
