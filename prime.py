# Function to check if number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Take input and check
n = int(input("Enter number: "))
print("Prime" if is_prime(n) else "Not Prime")
