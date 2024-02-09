# Given weight
weight = 45

# Cost variables for ground and drone shipping, and premium shipping cost
ground_shipping_cost = 0
drone_shipping_cost = 0
premium_shipping = 125

# Ground Shipping

# Calculating ground shipping cost based on weight
if weight <= 2:
    ground_shipping_cost += weight * 1.50 + 20
elif weight > 2 and weight <= 6:
    ground_shipping_cost += weight * 3 + 20
elif weight > 6 and weight <= 10:
    ground_shipping_cost += weight * 4 + 20
elif weight > 10:
    ground_shipping_cost += weight * 4.75 + 20
else:
    # This block should never execute, added for completeness
    print(ground_shipping_cost)

# Printing the cost of regular ground shipping
print("The cost of regular ground shipping is " + "$" + str(ground_shipping_cost))

# Printing the cost of premium ground shipping
print("The cost of premium ground shipping is " + "$" + str(premium_shipping))

# Drone Shipping

# Resetting weight for drone shipping calculation
weight = 45

# Calculating drone shipping cost based on weight
if weight <= 2:
    drone_shipping_cost += weight * 4.50
elif weight > 2 and weight <= 6:
    drone_shipping_cost += weight * 9
elif weight > 6 and weight <= 10:
    drone_shipping_cost += weight * 12
elif weight > 10:
    drone_shipping_cost += weight * 14.25 + 20
else:
    # This block should never execute, added for completeness
    print(drone_shipping_cost)

# Printing the cost of regular drone shipping
print("The cost of regular drone shipping is " + "$" + str(drone_shipping_cost))

# Comparing the costs of different shipping methods and providing a recommendation
if premium_shipping < ground_shipping_cost and premium_shipping < drone_shipping_cost:
    print("I recommend premium ground shipping as the cheapest option")
elif ground_shipping_cost < drone_shipping_cost:
    print("I recommend regular ground shipping as the cheapest option")
else:
    print("I recommend drone shipping as the cheapest option")