# First Project
# Define a function to compare the sums of two lists and return the list with the larger sum
def larger_sum(lst1, lst2):
    # Initialize variables to store the sums of the two lists
    sum1 = 0
    sum2 = 0
    
    # Calculate the sum of elements in the first list
    for num in lst1:
        sum1 += num
    
    # Calculate the sum of elements in the second list
    for num in lst2:
        sum2 += num
    
    # Compare the sums and return the list with the larger sum
    if sum1 > sum2:
        return lst1
    elif sum2 > sum1:
        return lst2
    else:
        # If the sums are equal, return the first list by default
        return lst1
# Test the function with two lists of numbers
print(larger_sum([1, 9, 5], [2, 3, 7]))


# Second Project
# Define a function to calculate the sum of elements in a list until the sum exceeds 9000
def over_nine_thousand(lst):
    # Initialize a variable to store the sum
    sum = 0
    
    # Iterate over each number in the list
    for num in lst:
        # Add the current number to the sum
        sum += num
        
        # Check if the sum exceeds 9000
        if sum > 9000:
            # If it does, break out of the loop
            break
    
    # Return the sum
    return sum
# Test the function with a list of numbers
print(over_nine_thousand([8000, 900, 120, 5000]))


# Third Project
# Define a function to find the maximum number in a list
def max_num(nums):
    # Initialize a variable to store the maximum value, assuming the first element is the maximum
    max_value = nums[0]
    
    # Iterate over each number in the list
    for num in nums:
        # Compare the current number with the maximum value
        if num > max_value:
            # If the current number is greater than the current maximum, update the maximum value
            max_value = num
    
    # Return the maximum value found
    return max_value
# Test the function with a list of numbers
print(max_num([50, -10, 0, 75, 20]))


# Fourth Project
# Define a function to find indices where corresponding elements in two lists are equal
def same_values(lst1, lst2):
    # Initialize an empty list to store indices where corresponding elements are equal
    new_lst= []
    
    # Iterate over the indices of the lists
    for index in range(len(lst1)):
        # Check if the elements at the current index in both lists are equal
        if lst1[index] == lst2[index]:
            # If they are equal, append the index to the new list
            new_lst.append(index)
    
    # Return the list of indices where corresponding elements are equal
    return new_lst
# Test the function with two lists of numbers
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# Fifth Project
# Define a function to find indices where corresponding elements in two lists are equal
def same_values(lst1, lst2):
    # Initialize an empty list to store indices where corresponding elements are equal
    new_lst= []
    
    # Iterate over the indices of the lists
    for index in range(len(lst1)):
        # Check if the elements at the current index in both lists are equal
        if lst1[index] == lst2[index]:
            # If they are equal, append the index to the new list
            new_lst.append(index)
    
    # Return the list of indices where corresponding elements are equal
    return new_lst
# Test the function with two lists of numbers
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))



