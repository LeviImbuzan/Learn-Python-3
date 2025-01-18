# First Project 
# Define a function named word_length_dictionary which takes a list of words as input
def word_length_dictionary(words):
    # Initialize an empty dictionary to store word-length pairs
    empty_dict = {}
    
    # Iterate over each word in the input list
    for string in words:
        # Update the dictionary with the word as key and its length as value
        empty_dict.update({string: len(string)})
    
    # Return the populated dictionary
    return "The dictionary " + str(words) + " has the following word lengths " + str(empty_dict)
# Uncommented function calls to test the word_length_dictionary function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# Expected output: {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# Expected output: {"a": 1, "": 0}


# Second Project
# Define a function named frequency_dictionary which takes a list of elements as input
def frequency_dictionary(words):
    # Create a new empty dictionary to store element-frequency pairs
    empty_dict = {}
    
    # Loop through every element in the input list
    for string in words:
        # Check if the string is NOT already in our dictionary
        if string not in empty_dict:
            # If the string is not in the dictionary, store it as a key with an initial frequency of 0
            empty_dict[string] = 0
        # Increment the frequency of the string by 1
        empty_dict[string] += 1
    
    # Return the dictionary containing element frequencies
    return "The frequency of dictionary " + str(words) + " is " + str(empty_dict)
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}



# Third Project
# Write your unique_values function here:

def unique_values(my_dictionary):
    # Initialize an empty list to store unique values
    empty_list = []
    
    # Iterate through the values in the dictionary
    for value in my_dictionary.values():
        # Check if the value is not already in the list
        if value not in empty_list:
            # If it's not in the list, append it to the list
            empty_list.append(value)
    
    # Return the number of unique values as a string
    return "The number of unique values in " + str(my_dictionary) + " is " + str(len(empty_list))
# Uncomment these function calls to test your function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


# Fourth Project
# Write your count_first_letter function here:

def count_first_letter(names):
    # Initialize an empty dictionary to store the counts of first letters
    letters = {}
    
    # Iterate through the keys (last names) in the names dictionary
    for key in names:
        # Get the first letter of each last name
        first_letter = key[0]
        
        # Check if the first letter is not already in the letters dictionary
        if first_letter not in letters:
            # If it's not in the dictionary, initialize its count to 0
            letters[first_letter] = 0
        
        # Increment the count of the first letter by the number of people with that last name
        letters[first_letter] += len(names[key])
    
    # Construct a string representing the result
    result_string = "The first letter is " + str(first_letter) + " and the number of people who have the same first letter in their last name is " + str(letters)
    
    # Return the result string
    return result_string
# Uncomment these function calls to test your function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
