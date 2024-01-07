# Import By deafult Library
from collections import Counter

user_input = input("Enter a string: ")

# Use Counter to count character frequencies
# char_frequency = Counter(user_input)

# Display the character frequency
for char in user_input:
    aa= user_input.count(char)
    print(f"Character '{char}' occurs {aa} times.")
