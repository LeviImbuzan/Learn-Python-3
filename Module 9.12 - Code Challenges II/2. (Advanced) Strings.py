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
