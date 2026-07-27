# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_table(number, limit=12):
    """Prints the multiplication table for a given number from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, limit + 1):
        print(f"{number:<2d}  x  {i:<2d}  =  {number * i}")
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
def part_a():
    """Generates a single multiplication table for a user-specified number."""
    print("\n--- PART A: Single Table ---")
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Error: Number must be a positive integer.")
            return
        
        print()
        print_table(num)
        
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
def part_b():
    """Generates multiplication tables for numbers from 1 to N."""
    print("\n--- PART B: Tables from 1 to N ---")
    try:
        n = int(input("Enter a number N: "))
        if n <= 0:
            print("Error: Number N must be a positive integer.")
            return
        
        print()
        for num in range(1, n + 1):
            print_table(num)
            # Add separator between tables
            if num < n:
                print("---------------------------")
                
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")
# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
def main():
    print("=========================================")
    print("     MULTIPLICATION TABLE GENERATOR      ")
    print("=========================================")
    print("1. Part A: Single Table")
    print("2. Part B: Bonus (Tables from 1 to N)")
    print("=========================================")
    choice = input("Select an option (1/2): ").strip()
    if choice == '1':
        part_a()
    elif choice == '2':
        part_b()
    else:
        print("Invalid choice. Exiting.")
if __name__ == "__main__":
    main()
Key Highlights:
Reusable Table Printer (print_table):
Uses a for loop ranging from 1 to 12.
Formats the table lines neatly using string formatting.
Part A:
Prompts for a number, validates that it is a positive integer (
N
>
0
N>0), and prints its table from 1 to 12.
Part B:
Prompts for 
N
N, validates 
N
>
0
N>0, and uses a for loop to generate tables for numbers 
1
,
2
,
…
,
N
1,2,…,N with separator lines between them.
The script has been saved to 
multiplication_table.py
.

12:13 PM
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
12:14 PM


Here is the complete Python solution for Assignment 7: Console-Based To-Do List Application.

Python Code Solution
python


def add_task(tasks):
    """Prompts the user for a task description and adds it to the list."""
    task_desc = input("Enter task: ").strip()
    if not task_desc:
        print("Task description cannot be empty.")
        return
    tasks.append(task_desc)
    print(f'Task added: "{task_desc}"')
def view_tasks(tasks):
    """Displays all tasks currently in the list, numbered from 1."""
    if not tasks:
        print("\nYour to-do list is currently empty.")
        return
    
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
def delete_task(tasks):
    """Displays tasks and prompts the user for a task number to remove."""
    if not tasks:
        print("\nYour to-do list is empty. Nothing to delete.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid numerical task number.")
def display_menu():
    """Prints the main application menu."""
    print("\n============================")
    print("     TO-DO LIST MENU        ")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
def main():
    tasks = []  # Master list storing task items
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose an option from 1 to 4.")
if __name__ == "__main__":
    main()
