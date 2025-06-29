# Function to check if a number is even or odd
def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Take input from user
num = int(input("Enter a number: "))
check_even_odd(num)
