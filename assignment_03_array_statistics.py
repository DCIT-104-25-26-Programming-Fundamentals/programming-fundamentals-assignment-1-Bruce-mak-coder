# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calc_sum(numbers):
    """Calculates the sum of a list of numbers without using built-in sum()."""
    total = 0.0
    for num in numbers:
        total += num
    return total
def calc_average(numbers):
    """Calculates the average of a list of numbers."""
    if len(numbers) == 0:
        return 0.0
    return calc_sum(numbers) / len(numbers)
def calc_maximum(numbers):
    """Finds the maximum value in a list of numbers without using built-in max()."""
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
def calc_minimum(numbers):
    """Finds the minimum value in a list of numbers without using built-in min()."""
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val
def main():
    try:
        count = int(input("How many numbers? "))
        
        # Validation: N must be a positive integer
        if count <= 0:
            print("Error: The count of numbers must be a positive integer greater than zero.")
            return
        # Read collection of numbers
        numbers = []
        for i in range(1, count + 1):
            val = float(input(f"Enter number {i}: "))
            numbers.append(val)
        # Helper to format display (displays integers without trailing decimals e.g., 23 instead of 23.0)
        def format_num(val):
            return int(val) if val.is_integer() else val
        # Calculate statistics
        total = calc_sum(numbers)
        avg = calc_average(numbers)
        maximum = calc_maximum(numbers)
        minimum = calc_minimum(numbers)
        # Output results
        print("\nResults:")
        print(f"Sum:     {format_num(total)}")
        print(f"Average: {format_num(avg)}")
        print(f"Maximum: {format_num(maximum)}")
        print(f"Minimum: {format_num(minimum)}")
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
if __name__ == "__main__":
    main()
