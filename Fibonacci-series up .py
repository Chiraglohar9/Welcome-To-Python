# Function to print Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Print first 10 Fibonacci numbers
fibonacci(10)
