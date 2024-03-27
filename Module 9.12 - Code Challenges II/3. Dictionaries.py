# First Project
# Define the sum_values function which calculates the sum of all values in a dictionary
def sum_values(my_dictionary):
    # Initialize a counter to store the sum of values
    counter = 0
    
    # Iterate over the values in the dictionary
    for price_value in my_dictionary.values():
        # Add each value to the counter
        counter += price_value
    
    # Return the sum of all values as a string
    return "The sum of all these products is $" + str(counter)
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6


# Second Project
# Define the sum_even_keys function which calculates the sum of values corresponding to even keys in a dictionary
def sum_even_keys(my_dictionary):
    # Initialize a counter to store the sum of values
    counter = 0
    
    # Iterate over the keys in the dictionary
    for keys in my_dictionary.keys():
        # Check if the key is even
        if keys % 2 == 0:
            # If the key is even, add the corresponding value to the counter
            counter += my_dictionary[keys]
    
    # Return the sum of values corresponding to even keys as a string
    return "The sum of even keys in this dictionary is " + str(counter)
# Uncomment these function calls to test your function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


# Third Project
# Define the add_ten function which increases the values of all keys in a dictionary by 10
def add_ten(my_dictionary):
    # Iterate over the keys in the dictionary
    for keys in my_dictionary.keys():
        # Increase the value corresponding to each key by 10
        my_dictionary[keys] += 10
    
    # Return the dictionary with values increased by 10 as a string
    return "This dictionary with values increased by 10 is " + str(my_dictionary)
# Uncomment these function calls to test your function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}



# Foruth Project
# Define the values_that_are_keys function which returns a list of values that are also keys in a dictionary
def values_that_are_keys(my_dictionary):
    # Initialize an empty list to store values that are also keys
    new_dictionary = []
    
    # Iterate over the values in the dictionary
    for values in my_dictionary.values():
        # Check if the value is also a key in the dictionary
        if values in my_dictionary:
            # If the value is also a key, append it to the new_dictionary list
            new_dictionary.append(values)
    
    # Return the list of values that are also keys
    return new_dictionary
# Uncomment these function calls to test your function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]


# Fifth Project
# Define the max_key function which returns the key associated with the maximum value in a dictionary
def max_key(my_dictionary):
    # Initialize variables to store the largest key and its corresponding value
    largest_key = float("-inf")  # Initialize largest_key to negative infinity
    largest_value = float("-inf")  # Initialize largest_value to negative infinity
    
    # Iterate over the key-value pairs in the dictionary
    for key, value in my_dictionary.items():
        # Check if the current value is greater than the largest_value found so far
        if value > largest_value:
            # If the current value is greater, update largest_value and largest_key
            largest_value = value
            largest_key = key
    
    # Return the largest_key found
    return "The largest key found is " + str(largest_key)
# Uncomment these function calls to test your function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


