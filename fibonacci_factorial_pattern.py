from testing_completion import fibonacci, factorial

def create_special_sequence(n):
    """
    Creates a special sequence combining Fibonacci and factorial numbers.
    For each position i, calculates: factorial(i) % fibonacci(i+2) if possible
    This creates an interesting pattern of numbers.
    
    Args:
        n (int): Length of the sequence to generate
        
    Returns:
        list: The special sequence
    """
    sequence = []
    for i in range(n):
        # We use i+2 for fibonacci to avoid division by zero
        # since fibonacci(0) and fibonacci(1) are 0 and 1
        fib_num = fibonacci(i + 2)
        fact_num = factorial(i)
        
        # Calculate the special number: factorial modulo fibonacci
        special_num = fact_num % fib_num
        sequence.append(special_num)
    return sequence

def analyze_sequence(sequence):
    """
    Analyzes the special sequence and prints interesting properties.
    
    Args:
        sequence (list): The sequence to analyze
    """
    print("Special Sequence Analysis:")
    print("-" * 40)
    print(f"Sequence: {sequence}")
    print(f"Length: {len(sequence)}")
    print(f"Max value: {max(sequence)}")
    print(f"Min value: {min(sequence)}")
    print(f"Average: {sum(sequence)/len(sequence):.2f}")
    
    # Find repeating patterns
    repeats = {}
    for i, num in enumerate(sequence):
        if num in repeats:
            repeats[num].append(i)
        else:
            repeats[num] = [i]
    
    print("\nRepeating numbers:")
    for num, positions in repeats.items():
        if len(positions) > 1:
            print(f"Number {num} appears at positions: {positions}")

def main():
    # Generate and analyze a sequence of 15 numbers
    sequence = create_special_sequence(15)
    analyze_sequence(sequence)
    
    # Visualize the sequence with a simple ASCII plot
    print("\nSequence visualization:")
    max_val = max(sequence)
    for num in sequence:
        stars = int((num / max_val) * 50)
        print(f"{num:4d} |{'*' * stars}")

if __name__ == "__main__":
    main()