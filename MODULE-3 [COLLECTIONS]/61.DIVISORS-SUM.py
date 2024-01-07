def sum_of_divisors(number):
    divisor_sum = 0

    for i in range(1, number + 1):
        if number % i == 0:
            divisor_sum += i

    return divisor_sum

# Example usage
number_to_check = int(input("Enter a number: "))
result = sum_of_divisors(number_to_check)

print(f"The sum of divisors of {number_to_check} is: {result}")
