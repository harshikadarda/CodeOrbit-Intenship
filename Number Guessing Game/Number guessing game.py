import random


def get_valid_guess(low, high):
    """
    Ask the user for a guess and keep asking until a valid integer
    within the allowed range is entered.
    """
    while True:
        raw_value = input(f"Enter your guess ({low}-{high}): ")
        try:
            guess = int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        return guess


def play_round(low=1, high=100):
    """
    Play a single round of the guessing game.
    Returns the number of attempts the player needed.
    """
    secret_number = random.randint(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}. Try to guess it!")

    while True:
        guess = get_valid_guess(low, high)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt(s).")
            return attempts


def ask_play_again():
    """Ask the user if they want to play another round."""
    while True:
        choice = input("\nPlay again? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def main():
    print("=== Number Guessing Game ===")

    total_rounds = 0
    total_attempts = 0

    while True:
        attempts = play_round(1, 100)
        total_rounds += 1
        total_attempts += attempts

        if not ask_play_again():
            break

    print("\n=== Game Summary ===")
    print(f"Rounds played: {total_rounds}")
    print(f"Total attempts: {total_attempts}")
    print(f"Average attempts per round: {total_attempts / total_rounds:.2f}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
