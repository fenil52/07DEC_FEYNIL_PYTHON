# Get an input character from the user  
character = input("Enter a character: ")  
  
# Creating a list of vowels  
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
  
# Check if the character is a vowel or not  
if character in vowels:  
    print("The character is a vowel!",character)  
else:  
    print(f"The character  is a consonant!",character)  