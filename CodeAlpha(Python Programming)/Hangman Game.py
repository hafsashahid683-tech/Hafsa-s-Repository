
import random


def play_hangman():
    # Five predefined words
    words = ["python", "apple", "school", "coding", "computer"]

    # Select a random word
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print("You have 6 incorrect guesses allowed.")

    while incorrect_guesses < max_attempts:
        # Display guessed and hidden letters
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

        # Check whether the player has won
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Enter one letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

    else:
        print("\nGame over! The word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
