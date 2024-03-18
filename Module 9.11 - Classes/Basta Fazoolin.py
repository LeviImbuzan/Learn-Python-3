# Define the Menu class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return 'This {menu} is available from {start_time} until {end_time}'.format(menu=self.name, start_time=self.start_time,end_time=self.end_time)
  
    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            total_price += self.items[item]
        return total_price

# Define menus for the franchise
brunch = Menu('Brunch Menu',{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)
early_bird = Menu('Early Bird Dinner Menu', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)
dinner = Menu('Dinner Menu', {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)
kids = Menu('Kids Menu', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

# Test calculate_bill method
print("The total price is $" + str(brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])))
print("The total price is $" + str(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])))

# Define the Franchise class
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus  

    def __repr__(self):
        return 'This {location} is {address}'.format(location=self.name, address=self.address)

    # Define method to get available menus based on time
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus

# Define menus for the franchise
menus = [brunch, early_bird, dinner, kids]

# Create instances of Franchise
flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)

# Test available_menus method
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

# Define the Business class
class Business:
    def __init__(self, franchise1, franchise2):
        self.franchise1 = franchise1
        self.franchise2 = franchise2

# Create instance of Business for "Basta Fazoolin' with my Heart"
basta_fazoolin = Business(flagship_store, new_installment)

# Define the menu for Take a' Arepa
arepas_menu = {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
}

# Create a Menu instance for Take a' Arepa
take_a_arepa = Menu("Take a' Arepa Menu", arepas_menu, 10, 20)

# Create a Franchise instance for Take a' Arepa
arepas_place = Franchise('189 Fitzgerald Avenue', [take_a_arepa])

# Add the Take a' Arepa franchise to the existing business
basta_fazoolin.franchise2 = arepas_place  # Assign the new franchise to franchise2 of the business
