# To-Do List CLI App

A simple command-line to-do list application built in Python. Users can add, view, and remove tasks, with tasks automatically saved to a text file so they persist between runs.

## Technologies Used
- **Python 3** (standard library only — no external dependencies)
- File I/O (`.txt` file) for task persistence

## Setup Instructions

1. **Install Python 3** (if not already installed)
   - Download from [python.org](https://www.python.org/downloads/) if needed.
   - Verify installation:
     ```bash
     python --version
     ```

2. **Get the project files**
   - Clone the repository (see link below) or download `todo_app.py` directly.

3. **Run the app**
   ```bash
   python todo_app.py
   ```

4. **Use the menu**
   - `1` → Add a task
   - `2` → View all tasks
   - `3` → Remove a task
   - `4` → Exit

   Tasks are automatically saved to `todo_list.txt` in the same folder, so they'll still be there next time you run the app.

## Sample Output

```
📋 Welcome to your To-Do List App!

========== TO-DO LIST MENU ==========
1. Add a task
2. View all tasks
3. Remove a task
4. Exit
======================================
Choose an option (1-4): 1
Enter the task you want to add: Buy groceries
✅ Task added: 'Buy groceries'

========== TO-DO LIST MENU ==========
1. Add a task
2. View all tasks
3. Remove a task
4. Exit
======================================
Choose an option (1-4): 1
Enter the task you want to add: Finish Python assignment
✅ Task added: 'Finish Python assignment'

========== TO-DO LIST MENU ==========
1. Add a task
2. View all tasks
3. Remove a task
4. Exit
======================================
Choose an option (1-4): 2

---------- YOUR TO-DO LIST ----------
1. Buy groceries
2. Finish Python assignment
--------------------------------------

========== TO-DO LIST MENU ==========
1. Add a task
2. View all tasks
3. Remove a task
4. Exit
======================================
Choose an option (1-4): 3

---------- YOUR TO-DO LIST ----------
1. Buy groceries
2. Finish Python assignment
--------------------------------------
Enter the task number to remove: abc
⚠️  Please enter a valid number.

========== TO-DO LIST MENU ==========
1. Add a task
2. View all tasks
3. Remove a task
4. Exit
======================================
Choose an option (1-4): 3

---------- YOUR TO-DO LIST ----------
1. Buy groceries
2. Finish Python assignment
--------------------------------------
Enter the task number to remove: 1
🗑️  Removed task: 'Buy groceries'

========== TO-DO LIST MENU ==========
1. Add a task
2. View all tasks
3. Remove a task
4. Exit
======================================
Choose an option (1-4): 4
👋 Goodbye! Your tasks have been saved.
```

## GitHub Repository Link
[https://github.com/harshikadarda/CodeOrbit-Intenship](https://github.com/harshikadarda/CodeOrbit-Intenship)
