def fibonacci(n, memo={0: 0, 1: 1}):
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

for i in range(10):
    print(fibonacci(i))


def factorial(n, acc=1):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return acc
    else:
        return factorial(n-1, n * acc)

for i in range(10):
    print(factorial(i))
