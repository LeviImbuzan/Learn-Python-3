# First Project
# Define a string containing all English letters in both uppercase and lowercase
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Define a function to count the number of unique English letters in a word
def unique_english_letters(word):
    # Initialize a variable to store the count of unique letters
    count = 0
    
    # Iterate through each letter in the predefined string of English letters
    for letter in letters:
        # Check if the current letter exists in the given word
        if letter in word:
            # If the letter exists in the word, increment the count
            count += 1
    
    # Return a string indicating the number of unique letters in the word
    return "The number of unique letters in " + str(word) + " is " + str(count)
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4


# Second Project
# Define a function to count occurrences of a specific character 'x' in a word
def count_char_x(word, x):
    # Initialize a counter variable to count occurrences of 'x'
    counter = 0
    
    # Iterate through each letter in the given word
    for letter in word:
        # Check if the current letter is equal to the character 'x'
        if letter == x:
            # If the letter matches 'x', increment the counter
            counter += 1
    
    # Return the count of occurrences of 'x' in the word
    return "The number of times " + str(x) + " appears in " + str(word) + " is " + str(counter)
# Uncomment these function calls to test your function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1


# Third Project
# Define a function to count occurrences of a multi-character string 'x' in a word
def count_multi_char_x(word, x):
    # Split the word by the multi-character string 'x'
    splits = word.split(x)
    
    # Count the number of splits (which corresponds to the number of occurrences of 'x') and subtract 1
    count = len(splits) - 1
    
    # Return a string indicating the number of times 'x' appears in 'word'
    return "The number of times " + str(x) + " appears in " + str(word) + " is " + str(count)
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


# Fourth Project
# Define a function to extract the substring between two specified letters in a word
def substring_between_letters(word, start, end):
    # Find the index of the first occurrence of the start letter
    first_index = word.find(start)
    
    # Find the index of the first occurrence of the end letter
    second_index = word.find(end)
    
    # Check if both start and end letters are found in the word
    if first_index > -1 and second_index > -1:
        # Extract the substring between the start and end letters
        # by slicing the word from the character after the start letter
        # to the character before the end letter
        return word[first_index + 1:second_index]
    
    # If either start or end letter is not found, return the original word
    return word
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


# Fifth Project
# Define a function to check if there are words of length at least 'x' in a sentence
def x_length_words(sentence, x):
    # Split the sentence into individual words
    words = sentence.split(" ")
    
    # Iterate through each word in the sentence
    for word in words:
        # Check if the length of the current word is at least 'x'
        if x <= len(word):
            # If a word of length at least 'x' is found, return True
            return True
        else:
            # If no word of length at least 'x' is found, return False
            return False
# Uncomment these function calls to test your function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
