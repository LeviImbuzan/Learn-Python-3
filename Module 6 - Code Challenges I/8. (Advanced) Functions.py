# First Project
def first_three_multiples(num):
    # Print the first multiple of num
    print(num * 1)
    # Print the second multiple of num
    print(num * 2)
    # Print the third multiple of num
    print(num * 3)
    # Return the third multiple of num
    return num * 3

# Test the function with num = 10
first_three_multiples(10)
# This call should print 10, 20, 30, and return 30
# Test the function with num = 0
first_three_multiples(0)
# This call should print 0, 0, 0, and return 0


# Second Project
def tip(total, percentage):
    # Calculate the tip amount based on the total and percentage
    return (total * percentage) / 100

# Test the function with total = 10 and percentage = 25
print(tip(10, 25))
# This call should print 2.5
# Test the function with total = 0 and percentage = 100
print(tip(0, 100))
# This call should print 0.0


# Third Project
def introduction(first_name, last_name):
    # Combine the first name, last name, and last name again with appropriate punctuation
    return last_name + ', ' + first_name + ' ' + last_name

# Test the function with first_name = "James" and last_name = "Bond"
print(introduction("James", "Bond"))
# This call should print Bond, James Bond
# Test the function with first_name = "Maya" and last_name = "Angelou"
print(introduction("Maya", "Angelou"))
# This call should print Angelou, Maya Angelou


# Fourth Project
def dog_years(name, age):
    # Convert human years to dog years by multiplying age by 7
    dog_age = age * 7
    # Create a string to display the dog's age
    return name + ", you are " + str(dog_age) + " years old in dog years"

# Test the function with name = "Lola" and age = 16
print(dog_years("Lola", 16))
# This call should print "Lola, you are 112 years old in dog years"
# Test the function with name = "Baby" and age = 0
print(dog_years("Baby", 0))
# This call should print "Baby, you are 0 years old in dog years"


# Fifth Project
def lots_of_math(a, b, c, d):
    # Calculate the sum of a and b
    first = a + b
    # Calculate the difference between c and d
    second = c - d
    # Calculate the product of first and second
    third = first * second
    # Print the values of first, second, and third
    print(first)
    print(second)
    print(third)
    # Return the remainder of third divided by a
    return third % a

# Test the function with a = 1, b = 2, c = 3, d = 4
print(lots_of_math(1, 2, 3, 4))
# This call should print 3, -1, -3, 0
# Test the function with a = 1, b = 1, c = 1, d = 1
print(lots_of_math(1, 1, 1, 1))
# This call should print 2, 0, 0, 0




