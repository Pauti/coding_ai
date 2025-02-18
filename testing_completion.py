def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = 1
        prev_fib = 0
        for i in range(2, n+1):
            temp = fib
            fib += prev_fib
            prev_fib = temp
        return fib

for i in range(10):
    print(fibonacci(i))


def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

for i in range(10):
    print(factorial(i))
