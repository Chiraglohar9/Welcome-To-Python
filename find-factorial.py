# Function to find factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Print factorial of 5
print("Factorial:", factorial(5))
