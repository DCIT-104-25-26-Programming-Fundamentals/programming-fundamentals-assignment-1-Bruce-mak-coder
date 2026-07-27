# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
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
