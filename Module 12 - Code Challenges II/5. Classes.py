# First Project
# Define the DriveBot class here!

class DriveBot:
    def __init__(self, motor_speed=0, sensor_range=0, direction=0):
        """
        Constructor for DriveBot class.

        Parameters:
        - motor_speed (int): The speed of the motor.
        - sensor_range (int): The range of sensors.
        - direction (int): The direction of the DriveBot.

        """
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

# Create an instance of DriveBot with specified parameters
robot_1 = DriveBot(5, 10, 90)

# Print out the attributes of the DriveBot instance
print("The motor speed is " + str(robot_1.motor_speed))
print("The direction is " + str(robot_1.direction))
print("The sensor range is " + str(robot_1.sensor_range))


# Second Project
class DriveBot:
    def __init__(self):
        """
        Constructor for DriveBot class.
        Initializes motor_speed, direction, and sensor_range attributes to 0.
        """
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
  
    def control_bot(self, new_speed, new_direction):
        """
        Method to control the DriveBot's speed and direction.

        Parameters:
        - new_speed (int): The new speed for the DriveBot.
        - new_direction (int): The new direction for the DriveBot.
        """
        self.motor_speed = new_speed
        self.direction = new_direction
    
    def adjust_sensor(self, new_sensor_range):
        """
        Method to adjust the sensor range of the DriveBot.

        Parameters:
        - new_sensor_range (int): The new sensor range for the DriveBot.
        """
        self.sensor_range = new_sensor_range
  

# Create an instance of DriveBot
robot_1 = DriveBot()

# Control the DriveBot's speed and direction
robot_1.control_bot(10, 180)

# Adjust the sensor range of the DriveBot
robot_1.adjust_sensor(20)

# Print out the updated attributes of the DriveBot instance
print("The new speed is " + str(robot_1.motor_speed))
print("The new direction is " + str(robot_1.direction))
print("The new sensor range is " + str(robot_1.sensor_range))


# Third Project
class DriveBot:
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        """
        Constructor for DriveBot class.

        Parameters:
        - motor_speed (int): The initial speed of the DriveBot. Default is 0.
        - direction (int): The initial direction of the DriveBot. Default is 180 degrees.
        - sensor_range (int): The initial sensor range of the DriveBot. Default is 10.
        """
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        """
        Method to control the DriveBot's speed and direction.

        Parameters:
        - new_speed (int): The new speed for the DriveBot.
        - new_direction (int): The new direction for the DriveBot.
        """
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        """
        Method to adjust the sensor range of the DriveBot.

        Parameters:
        - new_sensor_range (int): The new sensor range for the DriveBot.
        """
        self.sensor_range = new_sensor_range

# Create instances of DriveBot
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot()
robot_2.motor_speed = 35
robot_2.direction = 75
robot_2.sensor_range = 25

# Print out the attributes of robot_2
print("The new speed is " + str(robot_2.motor_speed))
print("The new direction is " + str(robot_2.direction))
print("The new sensor range is " + str(robot_2.sensor_range))


# Fourth Project
class DriveBot:
    # Class variables for DriveBot
    all_disabled = False  # Indicates if all DriveBots are disabled
    latitude = -999999  # Latitude coordinate
    longitude = -999999  # Longitude coordinate

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        """
        Constructor for DriveBot class.

        Parameters:
        - motor_speed (int): The initial speed of the DriveBot. Default is 0.
        - direction (int): The initial direction of the DriveBot. Default is 180 degrees.
        - sensor_range (int): The initial sensor range of the DriveBot. Default is 10.
        """
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        """
        Method to control the DriveBot's speed and direction.

        Parameters:
        - new_speed (int): The new speed for the DriveBot.
        - new_direction (int): The new direction for the DriveBot.
        """
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        """
        Method to adjust the sensor range of the DriveBot.

        Parameters:
        - new_sensor_range (int): The new sensor range for the DriveBot.
        """
        self.sensor_range = new_sensor_range

# Create instances of DriveBot
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Update class variables for all DriveBots
DriveBot.longitude = 50.0
DriveBot.latitude = -50
DriveBot.all_disabled = True

# Print out class variables of individual DriveBot instances
print("The latitude is " + str(robot_1.latitude))
print("The longitude is " + str(robot_2.longitude))
print(robot_3.all_disabled)


# Fifth Project
class DriveBot:
    # Class variables for DriveBot
    all_disabled = False  # Indicates if all DriveBots are disabled
    latitude = -999999  # Latitude coordinate
    longitude = -999999  # Longitude coordinate
    robot_count = 0  # Count of DriveBot instances

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        """
        Constructor for DriveBot class.

        Parameters:
        - motor_speed (int): The initial speed of the DriveBot. Default is 0.
        - direction (int): The initial direction of the DriveBot. Default is 180 degrees.
        - sensor_range (int): The initial sensor range of the DriveBot. Default is 10.
        """
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1  # Increment the robot count
        self.id = DriveBot.robot_count  # Assign unique ID to each DriveBot
    
    def control_bot(self, new_speed, new_direction):
        """
        Method to control the DriveBot's speed and direction.

        Parameters:
        - new_speed (int): The new speed for the DriveBot.
        - new_direction (int): The new direction for the DriveBot.
        """
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        """
        Method to adjust the sensor range of the DriveBot.

        Parameters:
        - new_sensor_range (int): The new sensor range for the DriveBot.
        """
        self.sensor_range = new_sensor_range

# Create instances of DriveBot
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Print out the IDs of each robot
print("This robot's ID number is " + str(robot_1.id))
print("This robot's ID number is " + str(robot_2.id))
print("This robot's ID number is " + str(robot_3.id))

