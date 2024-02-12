import random

name = ""
question = ""  # Here you can input your question
answer = ""
random_number = random.randint(1, 10)  # Generate a random number between 1 and 10

# Check if both name and question are empty
if name == "" and question == "":
    # Print an error message if both name and question are empty
    print("Error! You must ask a question and input your name")
# Check if name is empty
elif name == "":
    # Print the question and answer if name is empty
    print("Person asks: " + question + "\nMagic 8-Ball's answer: " + answer)
# Check if question is empty
elif question == "":
    # Print an error message if question is empty
    print("Error! You must ask a question")
else:
    # Print the question, name, and answer if both name and question are provided
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)

# Print a response based on the random number generated
if random_number == 1:
    print("Yes - definitely")
elif random_number == 2:
    print("It is decidedly so")
elif random_number == 3:
    print("Without a doubt")
elif random_number == 4:
    print("Reply hazy, try again")
elif random_number == 5:
    print("Ask again later")
elif random_number == 6:
    print("Better not tell you now")
elif random_number == 7:
    print("My sources say no")
elif random_number == 8:
    print("Outlook not so good")
elif random_number == 9:
    print("Very doubtful")
elif random_number == 10:
    print("Pray on it")
else:
    print("Error")  # Print an error message if the random number is out of expected range
