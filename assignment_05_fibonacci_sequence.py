# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# ============================================================================= YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
#
#  =============================================================================

def generate_fibonacci_terms(n):
    if n <= 0:
        return []
    terms = [0]
    if n == 1:
        return terms
    terms.append(1)
    while len(terms) < n:
        terms.append(terms[-1] + terms[-2])
    return terms


def is_fibonacci_number(value):
    if value < 0:
        return False
    a, b = 0, 1
    while a < value:
        a, b = b, a + b
    return a == value


def main():
    try:
        n = int(input("How many terms? "))
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    fibonacci_terms = generate_fibonacci_terms(n)
    print("Fibonacci sequence:", " ".join(str(term) for term in fibonacci_terms))

    try:
        value = int(input("Enter a number to check: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if is_fibonacci_number(value):
        print(f"{value} is a Fibonacci number.")
    else:
        print(f"{value} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()

