# List of toppings available
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# Prices of corresponding toppings
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of pizza slices priced at $2
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

# Calculate the total number of different kinds of pizzas available
num_pizzas = len(toppings)

# Print the total number of different kinds of pizzas available
print("We sell " + str(num_pizzas) + ' different kinds of pizza!')

# List of pizzas and their prices
pizza_and_prices = [[1, 'pepperoni'], [3, 'ham'], [4, 'pineapple'], [3, 'olives'], [8, "truffle"], [12, 'cavier'], [5, 'mushrooms']]
#print(len(pizza_and_prices))

# Insert a new pizza with its price at the beginning of the list
pizza_and_prices.insert(0, [2.5, 'peppers'])

# Sort the list of pizzas and their prices based on their prices
pizza_and_prices.sort()
#print(pizza_and_prices)

# Get the details of the cheapest pizza slice
cheapest_slice = pizza_and_prices[0]
print(cheapest_slice)

# Get the details of the priciest pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# Remove the last pizza from the list
pizza_and_prices.pop()

# Get the details of the three cheapest pizzas
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
