# First Project
# Define two numbers
num1 = 2
num2 = 8
# Check if the sum of the numbers is not equal to 10
if num1 + num2 != 10:
    # If the sum is not 10, assign True to the variable 'not_true'
    not_true = True
    # Print the value of 'not_true'
    print(not_true)
else:
    # If the sum is 10, assign False to the variable 'not_ten'
    not_ten = False
    # Print the value of 'not_ten'
    print(not_ten)


# First Project as Function
def not_sum_to_ten(num1, num2):
    # Check if the sum of num1 and num2 is not equal to 10
    if num1 + num2 != 10:
        # If the sum is not 10, return True
        return True
    else:
        # If the sum is 10, return False
        return False
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False


# Second Project
def over_budget(expense1, expense2, expense3, expense4, expense5):
    # Set the budget limit
    budget = 100
    
    # Calculate the total expenses
    total = expense1 + expense2 + expense3 + expense4 + expense5
    
    # Check if the total expenses exceed the budget
    if total >= budget:
        return True  # If total exceeds or equals the budget, return True
    else:
        return False  # If total is less than the budget, return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True


# Third Project
def large_power(base, exponent):
    # Check if the result of raising the base to the exponent power is greater than 5000
    if base ** exponent > 5000:
        return True  # If the result is greater than 5000, return True
    else:
        return False  # If the result is not greater than 5000, return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
    

# Fourth Project
def twice_as_large(num1, num2):
    # Check if num1 is greater than twice the value of num2
    if num1 > num2 * 2:
        return True  # If num1 is greater than twice num2, return True
    else:
        return False  # If num1 is not greater than twice num2, return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True


# Fifth Project
# Define the divisible_by_ten() function to check if a number is divisible by 10.
def divisible_by_ten(num):
    # Check if the number is divisible by 10 using the modulo operator (%).
    if num % 10 == 0:
        return True  # If the number is divisible by 10, return True.
    else:
        return False  # If the number is not divisible by 10, return False.
# Uncomment these print() function calls to test your divisible_by_ten() function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

