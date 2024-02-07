print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 7

# Write an if statement below:

if planet == 1:
  print("His weight on Venus would be " + str(weight * 0.91) + "lbs")
elif planet == 2:
  print("His weight on Mars would be " + str(weight * 0.38) + "lbs")
elif planet == 3:
  print("His weight on Jupiter would be " + str(weight * 2.34) + "lbs")
elif planet == 4:
  print("His weight on Saturn would be " + str(weight * 1.06) + "lbs")
elif planet == 5:
  print("His weight on Uranus would be " + str(weight * 0.92) + "lbs")
elif planet == 6:
  print("His weight on Neptne would be " + str(weight * 1.19) + "lbs")
else:
  print("Little Codey is only fighting contenders in this solar system!")