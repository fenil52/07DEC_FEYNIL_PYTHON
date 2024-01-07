def count_matching_strings(strings):
    count = 0

    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1

    return count

# Example usage:
string_list = ["abba", "python", "level", "radar", "hello", "civic"]
result = count_matching_strings(string_list)

print(f"Number of strings with length 2 or more and the same first and last character: {result}")
