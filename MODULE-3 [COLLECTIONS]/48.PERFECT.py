def is_perfect_number(number):
    divisors_sum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
    return divisors_sum == number

# Example usage
number_to_check = int(input("Enter a number: "))

if is_perfect_number(number_to_check):
    print(f"{number_to_check} is a perfect number.")
else:
    print(f"{number_to_check} is not a perfect number.")
