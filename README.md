# Python Mini Projects — 4-Day Challenge

A collection of four beginner-to-intermediate Python command-line applications, built one task per day. Each project is self-contained, uses only Python's standard library, and focuses on clean, well-commented, function-based code.

## Project Title

**Python Mini Projects: Calculator, To-Do List, Number Guessing Game & Contact Book**

## Technologies Used

- **Language:** Python 3.8+
- **Libraries:** Only the Python Standard Library
  - `random` — Number Guessing Game
  - `json` — Contact Book data storage
  - `os` — file existence checks (To-Do List, Contact Book)
- **Storage:** Plain text file (`tasks.txt`) and JSON file (`contacts.json`) — no external database required
- **Interface:** Command-Line Interface (CLI) for all four apps
- No third-party/pip packages are required — everything runs with a stock Python installation.

## Repository Structure

```
python-mini-projects/
│
├── task1_simple_calculator/
│   └── calculator.py
│
├── task2_todo_list_cli/
│   └── todo.py
│   └── tasks.txt          (auto-created when tasks are saved)
│
├── task3_number_guessing_game/
│   └── game.py
│
├── task4_contact_book/
│   └── contact_book.py
│   └── contacts.json      (auto-created when a contact is added)
│
└── README.md
```

## Task Overview

| Day | Task | Folder | Description |
|-----|------|--------|-------------|
| 1 | Simple Calculator | `task1_simple_calculator/` | Performs add, subtract, multiply, divide with input validation and division-by-zero handling. |
| 2 | To-Do List CLI App | `task2_todo_list_cli/` | Add, view, and remove tasks; optionally save/load tasks from `tasks.txt`. |
| 3 | Number Guessing Game | `task3_number_guessing_game/` | Guess a randomly picked number with "too high/too low" hints, attempt tracking, and multi-round play. |
| 4 | Contact Book (File-Based) | `task4_contact_book/` | Add, search, update, and delete contacts stored in `contacts.json`. |

### 1. Simple Calculator
- Performs basic arithmetic: addition, subtraction, multiplication, division.
- Takes user input through a menu and displays results clearly.
- Handles invalid (non-numeric) input and division-by-zero using `try`/`except`.
- Every function and logic block is commented for clarity.

### 2. To-Do List CLI App
- Add, view, and remove tasks through a simple menu.
- Tasks are kept in memory during runtime and can be saved to / loaded from `tasks.txt`.
- Tasks are displayed in a numbered, easy-to-read list.
- Each feature (add, view, remove, save, load) is organized into its own function.

### 3. Number Guessing Game
- The program randomly picks a number (default range: 1–100).
- After each guess, the player receives a "too high" or "too low" hint.
- The number of attempts is tracked and shown at the end of each round.
- A loop lets the player play as many rounds as they like.

### 4. Contact Book (File-Based)
- Add, search, update, and delete contacts (name, phone, email).
- All contacts are stored persistently in a human-readable JSON file (`contacts.json`).
- Search supports partial, case-insensitive name matching.
- Contacts are displayed in a clean, readable format.

## Setup Instructions

### Prerequisites
- [Python 3.8 or higher](https://www.python.org/downloads/) installed on your machine.
- Verify your installation:
  ```bash
  python --version
  # or
  python3 --version
  ```

### 1. Clone the Repository
```bash
git clone <GITHUB_REPOSITORY_LINK>
cd python-mini-projects
```

### 2. Run Any Project
No installation or dependencies are needed — just run the desired script with Python.

**Task 1 — Simple Calculator**
```bash
cd task1_simple_calculator
python calculator.py
```

**Task 2 — To-Do List CLI App**
```bash
cd task2_todo_list_cli
python todo.py
```

**Task 3 — Number Guessing Game**
```bash
cd task3_number_guessing_game
python game.py
```

**Task 4 — Contact Book**
```bash
cd task4_contact_book
python contact_book.py
```

> On some systems you may need to use `python3` instead of `python`.

### 3. Data Files
- `task2_todo_list_cli/tasks.txt` and `task4_contact_book/contacts.json` are created automatically the first time you save data — you don't need to create them manually.
- Both files are safe to delete if you want to reset a project's saved data.

## GitHub Repository Link

[https://github.com/harshikadarda/CodeOrbit-Intenship](https://github.com/harshikadarda/CodeOrbit-Intenship)

> Replace `<your-username>` (and the clone URL above) with your actual GitHub username/repository once this project is pushed.

## Author

Built as a 4-day, one-task-per-day Python practice challenge.
