import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman game with a list of words and optional number of lives."""
        self._word_list = word_list
        self._num_lives = num_lives
        self._initialize_game()

    def _initialize_game(self):
        """Initialize game attributes."""
        self._word = self._choose_word()
        self._word_guessed = ['_' for _ in self._word]
        self._num_letters = len(set(self._word))
        self._list_of_guesses = []

    def _choose_word(self):
        """Choose a random word from the word list."""
        return random.choice(self._word_list)

    def _update_word_guessed(self, guess):
        """Update the word_guessed list based on the guessed letter."""
        for i, letter in enumerate(self._word):
            if letter == guess:
                self._word_guessed[i] = guess
        self._num_letters -= 1

    def _handle_wrong_guess(self, guess):
        """Handle actions when the guess is not in the word."""
        self._num_lives -= 1
        print(f"Sorry, '{guess}' is not in the word.")
        print(f"You have {self._num_lives} lives left.")

    def check_guess(self, guess):
        """Check if the guessed letter is in the word and update the game state."""
        guess = guess.lower()

        if guess in self._word:
            print(f"Good guess! '{guess}' is in the word.")
            self._update_word_guessed(guess)
        else:
            self._handle_wrong_guess(guess)

    def ask_for_guess(self):
        """Prompt the user to guess a letter and validate the input."""
        while True:
            guess = input("Guess a letter: ")

            if len(guess) == 1 and guess.isalpha() and guess not in self._list_of_guesses:
                self._list_of_guesses.append(guess)
                break
            else:
                print("Invalid input. Please enter a single alphabetical character not tried before.")

    def play_game(self):
        """Main function to play the Hangman game."""
        while True:
            if self._num_lives == 0:
                print("You lost!")
                break
            elif self._num_letters > 0:
                self.ask_for_guess()
                self.check_guess(self._list_of_guesses[-1])
            else:
                print("Congratulations. You won the game!")
                break

# Outside the function, call your play_game function to play your game.
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    game.play_game()

# Testing the class
if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "grapes", "watermelon"]
    play_game(word_list)
