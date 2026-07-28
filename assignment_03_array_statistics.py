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

# =============================================================================  YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in

def calculate_sum(numbers): 
    total = 0
    for n in numbers:
        total += n
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers) if len(numbers) > 0 else 0

def calculate_maximum(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

def calculate_minimum(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for n in numbers:
        if n < min_num:
            min_num = n
    return min_num


def main():
    try:
        count = int(input("How many numbers? "))
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    if count <= 0:
        print("Error: number of values must be positive.")
        return

    numbers = []
    for i in range(1, count + 1):
        while True:
            try:
                number = float(input(f"Enter number {i}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        numbers.append(number)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_maximum(numbers)
    minimum = calculate_minimum(numbers)

    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


if __name__ == "__main__":
    main()

#  =============================================================================

