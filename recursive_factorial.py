# Recursive factorial calculation

# Recursive function
def recursive_factorial(n):
  if n == 1:
      return n
  else:
      return n * recursive_factorial(n-1)

# user input
n = 5

# check if the input is valid or not
if n < 0:
  print("Invalid input! Please enter a positive number.")
elif n == 0:
  print("Factorial of number 0 is 1")
else:
  print("Factorial of number", n, "=", recursive_factorial(n))