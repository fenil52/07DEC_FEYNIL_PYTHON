def is_in_range(number, lower_limit, upper_limit):
    if number >= lower_limit and number <= upper_limit:
     return True

# Example usage
number_to_check = int(input("Enter a number: "))
lower_limit = 1
upper_limit = 10

if is_in_range(number_to_check, lower_limit, upper_limit):
    print(f"{number_to_check} is in the range [{lower_limit}, {upper_limit}]")
else:
    print(f"{number_to_check} is NOT in the range [{lower_limit}, {upper_limit}]")
