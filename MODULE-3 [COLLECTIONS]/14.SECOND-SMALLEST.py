def second_smallest_number(input_list):
    sorted_list = sorted(input_list)
    print("Shorted Is :",sorted_list)
    return sorted_list[1]

# Example usage:
numbers = [30,10,80,3,12,1,5]
result = second_smallest_number(numbers)

print("Original List:", numbers)
print("Second Smallest Number:", result)
