# Iterative factorial calculation with a for loop
def iterative_for_factorial(n):
    result = 1
    if n > 1:
        for i in range(1, n+1):
            result = result * i
        return print(result)
    else:
        return print('N has to be positive')
        
iterative_for_factorial(7)
