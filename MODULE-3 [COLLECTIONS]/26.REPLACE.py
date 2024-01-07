list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# Replace the last value of each tuple with 99
modified_list_of_tuples = [(t[0], t[1],99) for t in list_of_tuples]

# Printing the result
print("Original List of Tuples:", list_of_tuples)
print("Modified List of Tuples:", modified_list_of_tuples)
