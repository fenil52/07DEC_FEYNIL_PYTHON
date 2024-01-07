# Sample string
sample_string = 'w3resource'
a=0

# Initialize an empty dictionary to store the letter counts
letter_counts = {}

# Iterate through each character in the string
for char in sample_string:
    a +=1
    letter_counts[char] = a
# Print the result
print("Sample String:", sample_string)
print("Letter Counts:", letter_counts)
