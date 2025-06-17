import random  # To select a random word from a list

# Step 1: List of possible words
word_list = ["apple", "banana", "orange", "grape", "cherry"]

# Step 2: Show word options to the player
print("🎮 Welcome to Hangman!")
print("Guess the hidden word, letter by letter!")
print("Possible words to choose from:", ", ".join(word_list))  # 👈 shows all the possible words

# Step 3: Randomly choose a word for the game
word = random.choice(word_list)

# Step 4: Set up for gameplay
guessed_letters = []  # To keep track of guessed letters
tries = 6  # Max wrong attempts allowed

# Step 5: Print blank placeholders for letters
print("\nWord to guess:")
print("_ " * len(word))  # Display underscores for each letter

# Step 6: Main game loop
while tries > 0:
    guess = input("\nEnter a single letter (a-z): ").lower()  # Take input and convert to lowercase

    # Step 7: Validate input
    if not guess.isalpha() or len(guess) != 1:
        print("❗ Invalid input. Please enter only ONE letter.")
        continue

    # Step 8: Check for repeated guesses
    if guess in guessed_letters:
        print("⏳ You already guessed that letter.")
        continue

    # Step 9: Add guess to list of guessed letters
    guessed_letters.append(guess)

    # Step 10: Check if guess is in the word
    if guess in word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print(f"❌ Wrong guess! You have {tries} tries left.")

    # Step 11: Show current progress of the word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word.strip())  # Clean spacing

    # Step 12: Check if all letters guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You've guessed the word correctly!")
        break
else:
    print("💀 Game Over! The correct word was:", word)
