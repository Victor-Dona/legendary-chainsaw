# Iterative factorial calculation with a while loop
def iterative_while_factorial(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return print(result)

iterative_while_factorial(5)


