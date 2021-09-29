import random
# Importing ascii images
from hangman_art import stages, logo 
# Importing list of words
from hangman_words import word_list
from replit import clear

# Print the hangman logo
print(logo)

# Win condition - Changes when player runs out of lives or guessed the word correctly
game_is_finished = False

# Player lives ... starting at 6
lives = len(stages) - 1

# Randomly choose a word from word list
chosen_word = random.choice(word_list)
# Get length of chosen word
word_length = len(chosen_word)

# List that keep tracks of player progress
display = []
# Add number of underscores based on word length
for _ in range(word_length):
    display += "_"

# Loop until game is finished 
while not game_is_finished:
    # Take a single letter input from user
    guess = input("Guess a letter: ").lower()

    # Use the clear() function imported from replit to clear the output between guesses.
    clear()

    # Check if the player already guessed that letter
    if guess in display:
        print(f"You've already guessed {guess}")

    # Loop and compare each letter in word with player's guess
    for position in range(word_length):
        # Get each letter in the word
        letter = chosen_word[position]
        # If the letter equals the player's letter
        if letter == guess:
            # Change the underscore to reveal the correctly guessed letter
            display[position] = letter
    print(f"{' '.join(display)}")

    # The player's guessed letter is not in the word
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        # Decrement the user's lives
        lives -= 1
        # If the player's live reaches 0, change end game condition to true
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    # There are no more underscores in the word -> User guessed all letters
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    # Print the ascii stage based on lives remaining
    print(stages[lives])