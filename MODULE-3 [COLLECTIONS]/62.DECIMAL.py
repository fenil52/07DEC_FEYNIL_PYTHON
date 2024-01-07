def find_max_min(numbers):
    if not numbers:
        return None, None

    return max(numbers), min(numbers)

# Example usage
decimal_numbers = [float(x) for x in input("Enter decimal numbers separated by spaces: ").split()]
max_num, min_num = find_max_min(decimal_numbers)

if max_num is not None and min_num is not None:
    print(f"The maximum number is: {max_num}")
    print(f"The minimum number is: {min_num}")
else:
    print("No numbers provided.")
