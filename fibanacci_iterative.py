def fibonacci_iterative(n):
    """
    Calculates the nth Fibonacci number using an iterative approach.
    This is more efficient than the recursive approach for larger n.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Get input from the user
try:
    num = int(input("Enter the value of n to find the nth Fibonacci number: "))
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        result = fibonacci_iterative(num)
        print(f"The {num}th Fibonacci number is: {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
