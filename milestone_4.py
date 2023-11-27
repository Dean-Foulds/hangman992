import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Step 3: Initialize attributes
        self.word_list = word_list
        self.word = self.choose_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def choose_word(self):
        """Choose a random word from the word list."""
        return random.choice(self.word_list)

    def check_guess(self, guess):
        """Check if the guessed letter is in the word and update the word_guessed."""
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess  # Replace "_" with the guessed letter
            self.num_letters -= 1  # Reduce the number of unique letters left to guess
        else:
            # Step 2: Handling when the guess is not in the word
            self.num_lives -= 1  # Reduce the number of lives
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

# Testing the extended check_guess method
if __name__ == "__main__":
    # Create an instance of the Hangman class
    hangman_game = Hangman(word_list=["apple", "banana", "orange", "grapes", "watermelon"])

    # Test the check_guess method with a wrong guess
    hangman_game.check_guess('z')
    print(f"Number of lives left: {hangman_game.num_lives}")

