# Number Guessing Game

A simple command-line game where the program picks a random number and the
user tries to guess it, receiving "too high" / "too low" hints after each
guess. The game tracks the number of attempts and lets the user play
multiple rounds in a row.

## Technologies Used

- Python 3 (standard library only — `random` module)

## Setup Instructions

1. Make sure Python 3.7+ is installed on your machine.
   ```bash
   python3 --version
   ```
2. Clone this repository (or copy the `number_guessing_game.py` file).
   ```bash
   git clone <repository-url>
   cd task3_number_guessing_game
   ```
3. Run the script:
   ```bash
   python3 number_guessing_game.py
   ```
4. Follow the on-screen prompts:
   - Enter a number between 1 and 100 when asked.
   - The game will tell you if your guess is too high or too low.
   - Once you guess correctly, your attempt count is shown.
   - Choose `y` to play another round or `n` to quit and see your summary.

## Sample Output

```
=== Number Guessing Game ===

I'm thinking of a number between 1 and 100. Try to guess it!
Enter your guess (1-100): 50
Too low! Try again.
Enter your guess (1-100): 75
Too low! Try again.
Enter your guess (1-100): 90
Too high! Try again.
Enter your guess (1-100): 82
Correct! The number was 82.
You guessed it in 4 attempt(s).

Play again? (y/n): n

=== Game Summary ===
Rounds played: 1
Total attempts: 4
Average attempts per round: 4.00
Thanks for playing!
```

## GitHub Repository Link

https://github.com/harshikadarda/CodeOrbit-Intenship
