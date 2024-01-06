def swap(str1, str2):
    # Swap the first two characters of each string
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    # Concatenate the strings with a space in between
    result_string = new_str1 + ' ' + new_str2

    return result_string


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result =swap(string1, string2)

print("Result:", result)
