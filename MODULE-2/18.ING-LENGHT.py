def modify_string(str):
    # Check if the length of the string is at least 3
    if len(str) >= 3:
        if str.endswith('ing'):
            result_str = str + 'ly'
        else:
            result_str = str + 'ing'
    else:
        result_str = str

    return result_str

user_input = input("Enter a string: ")
modified_string = modify_string(user_input)

print("Modified string:", modified_string)
