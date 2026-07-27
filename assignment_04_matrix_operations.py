# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def add_matrices(matrix_a, matrix_b):
    """
    Computes element-wise addition of two M x N matrices.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):          # Outer loop: iterate over rows
        row = []
        for j in range(cols):      # Inner loop: iterate over columns
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
def multiply_matrices(matrix_a, matrix_b):
    """
    Computes matrix multiplication: A (M x N) * B (N x P) -> Result (M x P).
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = []
    for i in range(rows_a):        # Loop over rows of A
        row = []
        for j in range(cols_b):    # Loop over columns of B
            sum_product = 0.0
            for k in range(cols_a):  # Dot product calculation
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            row.append(sum_product)
        result.append(row)
    return result
# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
def main():
    print("=========================================")
    print("       MATRIX OPERATIONS CALCULATOR       ")
    print("=========================================")
    print("1. Part A: Transpose a Matrix")
    print("2. Part B: Add Two Matrices")
    print("3. Part C: Multiply Two Matrices")
    print("=========================================")
    choice = input("Select an operation (1/2/3): ").strip()
    if choice == '1':
        print("\n--- Part A: Transpose Matrix ---")
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        mat = read_matrix(rows, cols, "Matrix")
        print("\nOriginal Matrix:")
        print_matrix(mat)
        transposed = transpose_matrix(mat)
        print("\nTransposed Matrix:")
        print_matrix(transposed)
    elif choice == '2':
        print("\n--- Part B: Add Two Matrices ---")
        rows = int(input("Enter number of rows for both matrices: "))
        cols = int(input("Enter number of columns for both matrices: "))
        mat_a = read_matrix(rows, cols, "Matrix A")
        mat_b = read_matrix(rows, cols, "Matrix B")
        print("\nMatrix A:")
        print_matrix(mat_a)
        print("\nMatrix B:")
        print_matrix(mat_b)
        result = add_matrices(mat_a, mat_b)
        print("\nSum (A + B):")
        print_matrix(result)
    elif choice == '3':
        print("\n--- Part C: Multiply Two Matrices ---")
        m = int(input("Enter number of rows for Matrix A (M): "))
        n = int(input("Enter number of columns for Matrix A / rows for Matrix B (N): "))
        p = int(input("Enter number of columns for Matrix B (P): "))
        mat_a = read_matrix(m, n, "Matrix A")
        mat_b = read_matrix(n, p, "Matrix B")
        print("\nMatrix A:")
        print_matrix(mat_a)
        print("\nMatrix B:")
        print_matrix(mat_b)
        result = multiply_matrices(mat_a, mat_b)
        print("\nProduct (A x B):")
        print_matrix(result)
    else:
        print("Invalid selection. Exiting.")
if __name__ == "__main__":
    main()
