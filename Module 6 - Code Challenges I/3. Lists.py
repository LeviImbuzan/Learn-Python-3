# First Project
def append_size(my_list):
    # Append the length of the list to the list itself
    my_list.append(len(my_list))
    return my_list
# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))


# Second Project
def append_sum(my_list):
    # Repeat the appending process three times
    for number_of_executions in range(3):
        # Calculate the sum of the last two elements of the list
        sums_added = my_list[-1] + my_list[-2]
        # Append the sum to the list
        my_list.append(sums_added)
    return my_list
# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


# Third Project
# Function to determine the larger list based on the number of elements
def larger_list(my_list1, my_list2):
    # Check if the length of the first list is greater
    if len(my_list1) > len(my_list2):
        return my_list1[-1]  # Return the last element of the first list
    # Check if the length of the second list is greater
    elif len(my_list2) > len(my_list1):
        return my_list2[-1]  # Return the last element of the second list
    else:
        return my_list1[-1]  # Return the last element of the first list if both have equal lengths
# Uncomment the lines below to test the function
print(larger_list([4, 10, 2, 5, 10], [-10, 2, 5, 10]))
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10, 8]))
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


# Fourth Project
# Function to check if an item appears more than n times in a list
def more_than_n(my_list, item, n):
    # Count the number of appearances of the item in the list
    number_of_appearances = my_list.count(item)
    # Check if the number of appearances is greater than n
    if number_of_appearances > n:
        return True  # Return True if item appears more than n times
    else:
        return False  # Return False otherwise
# Uncomment the line below to test the function
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# Fifth Project
# Function to combine and sort two lists
def combine_sort(my_list, my_list2):
    # Combine the lists
    combined_list = my_list + my_list2
    # Sort the combined list
    combined_list.sort()
    # Return the sorted combined list
    return combined_list
# Uncomment the line below to test the function
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))




