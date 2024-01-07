def have_common_member(list1, list2):
    common_elements = set(list1) & set(list2)
    return common_elements

# Example usage:
list_a = [1, 2, 3, 4]
list_b = [4,5, 6]

if have_common_member(list_a, list_b):
    print("The lists have at least one common member.")
else:
    print("The lists do not have a common member.")
