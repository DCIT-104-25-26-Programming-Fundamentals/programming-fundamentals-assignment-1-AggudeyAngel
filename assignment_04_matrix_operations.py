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
# =============================================================================YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def read_matrix(rows, cols, matrix_name=""):
    matrix = []
    for row_index in range(1, rows + 1):
        while True:
            row_input = input(f"Enter row {row_index} of {matrix_name}: ").strip()
            parts = row_input.split()
            if len(parts) != cols:
                print(f"Please enter exactly {cols} values.")
                continue
            try:
                row = [int(value) for value in parts]
                matrix.append(row)
                break
            except ValueError:
                print("Invalid row. Please enter only integers separated by spaces.")
    return matrix


def display_matrix(matrix):
    if not matrix:
        print("[]")
        return
    column_width = 0
    for row in matrix:
        for value in row:
            column_width = max(column_width, len(str(value)))
    for row in matrix:
        row_text = " ".join(f"{value:>{column_width}}" for value in row)
        print(row_text)


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for col_index in range(cols):
        new_row = []
        for row_index in range(rows):
            new_row.append(matrix[row_index][col_index])
        transposed.append(new_row)
    return transposed


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for row_index in range(rows):
        result_row = []
        for col_index in range(cols):
            result_row.append(matrix_a[row_index][col_index] + matrix_b[row_index][col_index])
        result.append(result_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = []
    for row_index in range(rows_a):
        result_row = []
        for col_index in range(cols_b):
            total = 0
            for inner_index in range(cols_a):
                total += matrix_a[row_index][inner_index] * matrix_b[inner_index][col_index]
            result_row.append(total)
        result.append(result_row)
    return result


def main():
    print("PART A — Transpose a Matrix")
    rows = read_int("Enter number of rows: ")
    cols = read_int("Enter number of columns: ")
    matrix = read_matrix(rows, cols)
    print("\nOriginal Matrix:")
    display_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transpose_matrix(matrix))

    print("\nPART B — Add Two Matrices")
    rows = read_int("Enter number of rows: ")
    cols = read_int("Enter number of columns: ")
    matrix_a = read_matrix(rows, cols, "matrix A")
    matrix_b = read_matrix(rows, cols, "matrix B")
    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)
    print("\nSum of matrices:")
    display_matrix(add_matrices(matrix_a, matrix_b))

    print("\nPART C — Multiply Two Matrices")
    rows_a = read_int("Enter number of rows for matrix A: ")
    cols_a = read_int("Enter number of columns for matrix A: ")
    rows_b = read_int("Enter number of rows for matrix B: ")
    cols_b = read_int("Enter number of columns for matrix B: ")
    if cols_a != rows_b:
        print("Error: number of columns in matrix A must equal number of rows in matrix B.")
        return
    matrix_a = read_matrix(rows_a, cols_a, "matrix A")
    matrix_b = read_matrix(rows_b, cols_b, "matrix B")
    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)
    print("\nProduct A × B:")
    display_matrix(multiply_matrices(matrix_a, matrix_b))


if __name__ == "__main__":
    main()


#  =============================================================================

