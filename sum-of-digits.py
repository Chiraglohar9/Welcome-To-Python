# Function to find the sum of digits of a number
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Get last digit
        n //= 10         # Remove last digit
    return total

# Call the function
print("Sum of digits:", sum_of_digits(1234))
