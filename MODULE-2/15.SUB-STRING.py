def count_substring(main_string, substring):
    return main_string.count(substring)

# Example usage
main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

occurrences = count_substring(main_string, substring)

print(f"The substring '{substring}' occurs {occurrences} times in the main string.")
