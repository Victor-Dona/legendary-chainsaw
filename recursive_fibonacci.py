# Recursive Fibonnaci Sequence
# Given a number n, find the index n-th number it represents in the Fibonnaci sequence

def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
    
def fibonacci_input():
    n = int(input('Input number to find in Fibonacci sequence: '))
    print(recursive_fibonacci(n))

fibonacci_input()
