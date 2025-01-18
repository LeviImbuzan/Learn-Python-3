# List of hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Prices of each hairstyle
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Number of each hairstyle sold last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate the total price of all haircuts
total_price = 0
for price in prices:
    total_price += price
print("Total price is: $" + str(total_price))

# Calculate the average price of haircuts
average_price = total_price / len(prices)
print("Average Haircut Price: $" + str(average_price))

# Calculate new prices after reducing $5 from each price
new_prices = [price - 5 for price in prices]

# Calculate the total revenue generated from all haircuts
total_revenue = 0 
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue: $" + str(total_revenue))

# Calculate the average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: $" + str(average_daily_revenue))

# Find the hairstyles with prices under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Cuts under $30 are: " + str(cuts_under_30))
