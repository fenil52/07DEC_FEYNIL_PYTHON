import heapq

def highest_values(dictionary, n=3):
    # Use nlargest to get the highest values
    highest = heapq.nlargest(n, dictionary.values())
    
    # Create a dictionary with only the entries having the highest values
    result = {key:f"{value}" for key, value in dictionary.items() if value in highest}
    
    return result

# Example dictionary
my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 25, 'e': 15}

# Find the highest 3 values
highest_values_dict = highest_values(my_dict)

# Print the result
print("Original Dictionary:", my_dict)
print("Highest 3 Values:", highest_values_dict)

