import random
from pathlib import Path


WORD_LIST_PATH = Path(__file__).with_name("google-10000-english-no-swears.txt")
MAX_ATTEMPTS = 6

HANGMAN_PICS = (
    " +---+\n"
    " |   |\n"
    "     |\n"
    "     |\n"
    "     |\n"
    "     |\n"
    "=========",
    " +---+\n"
    " |   |\n"
    " O   |\n"
    "     |\n"
    "     |\n"
    "     |\n"
    "=========",
    " +---+\n"
    " |   |\n"
    " O   |\n"
    " |   |\n"
    "     |\n"
    "     |\n"
    "=========",
    " +---+\n"
    " |   |\n"
    " O   |\n"
    "/|   |\n"
    "     |\n"
    "     |\n"
    "=========",
    " +---+\n"
    " |   |\n"
    " O   |\n"
    "/|\\  |\n"
    "     |\n"
    "     |\n"
    "=========",
    " +---+\n"
    " |   |\n"
    " O   |\n"
    "/|\\  |\n"
    "/    |\n"
    "     |\n"
    "=========",
    " +---+\n"
    " |   |\n"
    " O   |\n"
    "/|\\  |\n"
    "/ \\  |\n"
    "     |\n"
    "=========",
)


def load_words(path=WORD_LIST_PATH):
    """Load usable words from the word list beside this script."""
    with path.open(encoding="utf-8") as word_file:
        words = [
            line.strip().lower()
            for line in word_file
            if line.strip().isalpha() and line.strip().isascii()
        ]

    if not words:
        raise ValueError(f"No usable words found in {path}")
    return words


def play():
    secret_word = random.choice(load_words())
    guessed_letters = set()
    incorrect_guesses = 0

    print("Welcome to Hangman!")

    while incorrect_guesses < MAX_ATTEMPTS:
        print()
        print(HANGMAN_PICS[incorrect_guesses])
        print("Word: " + " ".join(
            letter if letter in guessed_letters else "_" for letter in secret_word
        ))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'none'}")
        print(f"Attempts remaining: {MAX_ATTEMPTS - incorrect_guesses}")

        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Please enter a single English letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)
        if guess not in secret_word:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
        else:
            print(f"Good guess! '{guess}' is in the word.")

        if all(letter in guessed_letters for letter in secret_word):
            print()
            print(HANGMAN_PICS[incorrect_guesses])
            print(f"You win! The word was '{secret_word}'.")
            return

    print()
    print(HANGMAN_PICS[MAX_ATTEMPTS])
    print(f"Game over! The word was '{secret_word}'.")


if __name__ == "__main__":
    play()
