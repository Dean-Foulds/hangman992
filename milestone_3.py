import random

secret_word = "apple"  # Assume the secret word is "apple" for demonstration purposes.

def check_guess(guess):
    """Check if the guessed letter is in the word."""
    guess = guess.lower()  # Step 2: Convert the guess into lower case.

    # Step 3: Move the code to check if the guess is in the word into this function block.
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    """Ask the user to guess a letter and validate the input."""
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Step 3: Call the check_guess function to check if the guess is in the word.
    check_guess(guess)

# Step 4: Call the ask_for_input function to test your code.
ask_for_input()

