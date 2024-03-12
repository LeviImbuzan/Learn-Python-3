# Define the letters of the alphabet and their corresponding points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create a dictionary mapping letters to their corresponding points
letter_to_points = dict(zip(letters, points))
letter_to_points[" "] = 0  # Add a space with 0 points

# Define a function to calculate the points for a word
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)  # Look up the points for each letter in the word
    return point_total

# Initial mapping of players to the words they've played
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi_Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof_Reader": ["ZAP", "COMA", "PERIOD"]
}

# Dictionary to store the points earned by each player
player_to_points = {}

# Calculate points for each player based on the words they've played
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

# Print the points earned by each player
print(player_to_points)

# Define a function to add a word played by a player to their list of words
def play_word(player, word, player_to_words):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]

# Test the play_word() function
#play_word("player1", "BALL", player_to_words)
#print(player_to_words)
