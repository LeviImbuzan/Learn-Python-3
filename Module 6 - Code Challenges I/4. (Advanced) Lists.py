# First Project
# Define a function named every_three_nums that takes a start number as input
def every_three_nums(start):
    # Create a list of numbers starting from 'start' up to 100 with a step of 3
    list_nums = range(start, 101, 3)
    # Convert the range object to a list and return it
    return list(list_nums)
# Uncomment the line below when your function is done
print(every_three_nums(91))


# Second Project
# Define a function named remove_middle that removes elements from a list between the indices 'start' and 'end'
def remove_middle(my_list, start, end):
    # Return a new list by concatenating the elements before 'start' and after 'end' indices
    return my_list[:start] + my_list[end+1:]
# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# Third Project
# Define a function named more_frequent_item that returns the more frequent item between item1 and item2 in my_list
def more_frequent_item(my_list, item1, item2):
    # Count occurrences of item1 and item2 in my_list
    count_one = my_list.count(item1)
    count_two = my_list.count(item2)
    # Compare counts and return the item with the higher count
    if count_one > count_two:
        return item1
    elif count_two > count_one:
        return item2
    else:
        return item1
# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# Fourth Project
# Define a function named double_index that doubles the value of the element at index 'index' in my_list
def double_index(my_list, index):
    # Check if the index is out of bounds
    if index >= len(my_list):
        return my_list
    else:
        # Create a new list containing elements up to the specified index
        new_list = my_list[:index] 
        # Double the value at the specified index and append it to the new list
        new_list.append(my_list[index]*2)
    # Concatenate the new list with elements after the specified index and return it
    my_new_list = new_list + my_list[index+1:]
    return my_new_list
# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))


# Fifth Project
# Define a function named middle_element that returns the middle element(s) of a list
def middle_element(my_list):
    # Check if the length of the list is even
    if len(my_list) % 2 == 0:
        # Calculate the sum of the two middle elements and return their average
        sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
        return sum / 2
    else:
        # If the length of the list is odd, return the middle element
        return my_list[int(len(my_list)/2)]
# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))


