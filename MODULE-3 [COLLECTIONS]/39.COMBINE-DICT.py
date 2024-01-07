from collections import Counter

# Given dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries and add values for common keys
combined_counter = Counter(d1) + Counter(d2)

# Printing the result
print("Combined Counter:", combined_counter)
