def fibonacci_memoization(n, memo={}):
    """
    Calculates the nth Fibonacci number using recursion with memoization
    (dynamic programming).
    """
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
        return memo[n]

# Get input from the user
try:
    num = int(input("Enter the value of n to find the nth Fibonacci number: "))
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        result = fibonacci_memoization(num)
        print(f"The {num}th Fibonacci number is: {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
