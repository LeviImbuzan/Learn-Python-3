# First Project
# Write your check_for_name function here:
def check_for_name(sentence, name):
    # Convert both the sentence and the name to lowercase for case-insensitive comparison
    lower_sentence = sentence.lower()
    lower_name = name.lower()

    # Split the sentence into individual words
    split_sentence = lower_sentence.split()

    # Iterate through each word in the split sentence
    for word in split_sentence:
        # Check if the lowercase name matches any word in the sentence
        if lower_name == word:
            return str(name) + " is in the sentence " + str(sentence) + " - " + str(True)  # If a match is found, return True
    
    # If no match is found after checking all words, return False
    return str(name) + " is not in the sentence " + str(sentence) + " - " + str(False)

# Uncomment these function calls to test your function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# Second Project
# Write your every_other_letter function here:
def every_other_letter(word):
    # Initialize an empty string to store the new string containing every other letter
    new_string = ""
    
    # Iterate through the indices of the characters in the word
    for letter in range(len(word)):
        # Check if the index is even, indicating every other letter
        if letter % 2 == 0:
            # Concatenate the character at the even index to the new string
            new_string += word[letter]
    
    # Return the new string containing every other letter
    return "Every other word in " +str(word) + " is " + str(new_string)
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print an empty string


# Third Project
# Write your reverse_string function here:
def reverse_string(word):
    # Initialize an empty string to store the reversed string
    reversed_string = ""

    # Loop through the characters of the word starting from the last character
    for letter in range(len(word) - 1, -1, -1):
        # Append each character to the reversed string
        reversed_string += word[letter]

    # Return the reversed string
    return "The reverse of " + str(word) + " is " + str(reversed_string)
# Uncomment these function calls to test your function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print an empty string



# Fourth Project
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    # Extract the first character of each word
    first_character = word1[0]
    second_character = word2[0]
    
    # Extract the remaining characters of each word
    first_remaining_characters = word1[1:]
    second_remaining_characters = word2[1:]
    
    # Combine the first character of the second word with the remaining characters of the first word
    first_word = second_character + first_remaining_characters + ' '
    
    # Combine the first character of the first word with the remaining characters of the second word
    second_word = first_character + second_remaining_characters 
    
    # Return the combined string
    return "The spoonerism of these words is " + str(first_word) + str(second_word)
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


# Fifth Project
# Define the add_exclamation function which adds exclamation marks to a word until its length reaches 20 characters
def add_exclamation(word):
    # Loop until the length of the word reaches 20 characters
    while len(word) < 20:
        # Add an exclamation mark to the end of the word
        word += '!'
    # Return the modified word
    return "This word is now 20 characters long - " + word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
