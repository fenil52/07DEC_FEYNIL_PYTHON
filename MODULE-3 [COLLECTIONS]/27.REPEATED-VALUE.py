# Example tuple
my_tuple = (1, 2, 3, 2, 4, 5, 4, 6, 7)

# Find repeated items in the tuple
repeated_items = set(item for item in my_tuple if my_tuple.count(item)>1)

# Printing the result
print("Original Tuple:", my_tuple)
print("Repeated Items:", repeated_items)
