# Function to convert Fahrenheit to Celsius
def f_to_c(f_temp):
    # Formula for conversion
    c_temp = (f_temp - 32) * 5/9
    return c_temp

# Test conversion of 100°F to Celsius
f100_in_celsius = f_to_c(100)
print("That temperature in Celsius is " + str(round(f100_in_celsius)) + " degrees.")

# Function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
    # Formula for conversion
    f_temp = (c_temp * 9/5) + 32
    return f_temp

# Test conversion of 0°C to Fahrenheit
c0_in_fahrenheit = c_to_f(0)
print("That temperature in Fahrenheit is " + str(round(c0_in_fahrenheit)) + " degrees.")

# Function to calculate force
def get_force(mass, acceleration):
    # Formula for force
    return mass * acceleration

# Constants related to the train
train_mass = 22680  # mass of the train in kg
train_acceleration = 10  # acceleration of the train in m/s^2

# Calculate the force exerted by the train
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Function to calculate energy
def get_energy(mass, c=3*10**8):
    # Formula for energy (E=mc^2)
    return mass * c**2

# Constants related to the bomb
bomb_mass = 1  # mass of the bomb in kg

# Calculate the energy released by the bomb
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Function to calculate work
def get_work(mass, acceleration, distance):
    # Calculate force using given mass and acceleration
    force = get_force(mass, acceleration)
    # Calculate work using the formula (work = force * distance)
    return force * distance

# Constants related to the train's movement
train_distance = 100  # distance traveled by the train in meters

# Calculate the work done by the train over a certain distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
