def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# Example usage
result_iterative = factorial_iterative(5)
print("Factorial (Iterative):", result_iterative)
