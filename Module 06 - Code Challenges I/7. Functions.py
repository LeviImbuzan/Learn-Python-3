# First Project
def tenth_power(num):
    # raise the number to the power of 10
    num = num**10
    # return the result
    return round(num)
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# Second Project
def square_root(num):
    # take the square root of the given number
    num = num**0.5
    # return the result
    return round(num)
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10


# Third Project
def win_percentage(wins, losses):
    # calculate the total number of games
    total_games = wins + losses
    # calculate the win percentage
    ratio = (wins/total_games) * 100
    # return the win percentage
    return round(ratio)
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


# Fourth Project
def average(num1, num2):
    # calculate the sum of the two numbers and divide by 2 to find the average
    sum = (num1 + num2)/2
    # return the calculated average
    return round(sum)
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0


# Fifth Project
def remainder(num1, num2):
    # double the first number
    num1 = num1*2
    # halve the second number
    num2 = num2/2
    # calculate the remainder when the doubled first number is divided by the halved second number
    remainder = num1 % num2
    # round the remainder and return it
    return round(remainder)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))



