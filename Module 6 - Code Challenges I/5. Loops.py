# First Project
def divisible_by_ten(nums):
    # Initialize a variable to count the numbers divisible by ten
    count = 0
    
    # Iterate through each number in the list
    for num in nums:
        # Check if the number is divisible by ten
        if num % 10 == 0:
            # If it is, increment the count
            count += 1
    
    # Return the count of numbers divisible by ten
    return count
# Test the function with a list of numbers
print(divisible_by_ten([20, 25, 30, 35, 40]))


# Second Project
def add_greetings(names):
    # Initialize an empty list to store greetings
    greeting_list = []
    
    # Iterate through each name in the input list
    for name in names:
        # Concatenate "Hello, " with the current name and append it to the greeting list
        greeting_list.append("Hello, " + name)
    
    # Return the list of greetings
    return greeting_list
# Test the function with a list of names
print(add_greetings(["Owen", "Max", "Sophie"]))


# Third Project
# Define a function to delete starting even numbers from a list
def delete_starting_evens(my_list):
    # Iterate over each number in the list
    for num in my_list:
        # Check if the current number is even
        if num % 2 == 0:
            # If it is even, remove the first element from the list
            my_list = my_list[1:]
        else:
            # If the current number is odd, exit the loop
            break
    # Return the modified list
    return my_list

# Test the function with a list of numbers
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# Fourth Project
# Define a function to return elements at odd indices from a list
def odd_indices(my_list):
    # Initialize an empty list to store elements at odd indices
    my_new_list = []
    
    # Iterate over the indices of the list starting from 1 (the second element) with a step of 2 (to get odd indices)
    for index in range(1, len(my_list), 2):
        # Append the element at the current odd index to the new list
        my_new_list.append(my_list[index])
    
    # Return the list containing elements at odd indices
    return my_new_list
# Test the function with a list of numbers
print(odd_indices([4, 3, 7, 10, 11, -2]))


# Fifth Project
# Define a function to calculate exponents of bases raised to powers
def exponents(bases, powers):
    # Initialize an empty list to store the results
    new_list = []
    
    # Iterate over each base in the bases list
    for base in bases:
        # Iterate over each power in the powers list
        for power in powers:
            # Calculate the result of raising the current base to the current power and append it to the new list
            new_list.append(base ** power)
    
    # Return the list containing all the exponentiation results
    return new_list
# Test the function with lists of bases and powers
print(exponents([2, 3, 4], [1, 2, 3]))




