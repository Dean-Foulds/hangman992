import random

def choose_secret_word():
    """Choose a random secret word for the game."""
    words = ["apple", "banana", "orange", "grapes", "watermelon"]
    return random.choice(words)

def check_guess(secret_word, guess):
    """Check if the guessed letter is in the word."""
    guess = guess.lower()

    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_guess():
    """Prompt the user to guess a letter and validate the input."""
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid input. Please enter a single alphabetical character.")

    return guess

def play_game():
    """Main function to play the guessing game."""
    secret_word = choose_secret_word()

    while True:
        guess = ask_for_guess()
        check_guess(secret_word, guess)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()


