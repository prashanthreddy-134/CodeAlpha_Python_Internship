import random
WORDS = ["python", "developer", "internship", "keyboard", "program"]
MAX_WRONG_GUESSES = 6
HANGMAN_STAGES = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
]
def show_board(secret, guessed, wrong):
    masked = " ".join(letter if letter in guessed else "_" for letter in secret)
    print(HANGMAN_STAGES[len(wrong)])
    print("\nWord:", masked)
    print("Wrong guesses:", ", ".join(wrong) if wrong else "None")
    print(f"Lives left: {MAX_WRONG_GUESSES - len(wrong)}\n")
def get_guess(guessed, wrong):
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
        elif guess in guessed or guess in wrong:
            print(f"You already guessed '{guess}'. Try another letter.")
        else:
            return guess
def play_round():
    secret = random.choice(WORDS)
    guessed = []   # correct letters
    wrong = []     # incorrect letters
    print("\nNew word is ready! It has", len(secret), "letters.")
    while True:
        show_board(secret, guessed, wrong)
        if all(letter in guessed for letter in secret):
            print(f"Congratulations! You guessed the word: {secret.upper()}")
            return True
        if len(wrong) >= MAX_WRONG_GUESSES:
            print(f"Game over! The word was: {secret.upper()}")
            return False
        guess = get_guess(guessed, wrong)
        if guess in secret:
            guessed.append(guess)
            print("Good guess!")
        else:
            wrong.append(guess)
            print("Wrong guess!")
def main():
    print("=== HANGMAN ===")
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()
