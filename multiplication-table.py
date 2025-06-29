# Function to print multiplication table of a number
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# Take input and print table
table(int(input("Enter number: ")))
