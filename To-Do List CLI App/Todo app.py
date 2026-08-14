import os

# Name of the file used to persist tasks between runs
FILE_NAME = "todo_list.txt"


def load_tasks():
    """
    Load tasks from the text file (if it exists) into a list.
    Each line in the file represents one task.
    Returns a list of task strings.
    """
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            # Read each line, strip newline characters, ignore empty lines
            tasks = [line.strip() for line in file.readlines() if line.strip()]
    return tasks


def save_tasks(tasks):
    """
    Save the current list of tasks to the text file.
    Overwrites the file each time to keep it in sync with memory.
    """
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    """
    Prompt the user for a new task and add it to the list.
    """
    task = input("Enter the task you want to add: ").strip()
    if task == "":
        print("⚠️  Task cannot be empty. Nothing was added.\n")
        return
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: '{task}'\n")


def view_tasks(tasks):
    """
    Display all current tasks in a numbered, readable format.
    """
    print("\n---------- YOUR TO-DO LIST ----------")
    if not tasks:
        print("No tasks yet. Add one from the menu!")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("--------------------------------------\n")


def remove_task(tasks):
    """
    Show the list, ask which task number to remove,
    validate the input, and remove the task if valid.
    """
    view_tasks(tasks)
    if not tasks:
        return  # Nothing to remove

    choice = input("Enter the task number to remove: ").strip()

    # Validate that the input is a number
    if not choice.isdigit():
        print("⚠️  Please enter a valid number.\n")
        return

    choice = int(choice)

    # Validate that the number is within range
    if 1 <= choice <= len(tasks):
        removed = tasks.pop(choice - 1)
        save_tasks(tasks)
        print(f"🗑️  Removed task: '{removed}'\n")
    else:
        print("⚠️  Invalid task number.\n")


def show_menu():
    """
    Display the main menu options to the user.
    """
    print("========== TO-DO LIST MENU ==========")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Exit")
    print("======================================")


def main():
    """
    Main program loop that ties all features together.
    """
    tasks = load_tasks()  # Load any previously saved tasks
    print("📋 Welcome to your To-Do List App!\n")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Goodbye! Your tasks have been saved.")
            break
        else:
            print("⚠️  Invalid choice. Please select 1, 2, 3, or 4.\n")


# Entry point of the program
if __name__ == "__main__":
    main()
