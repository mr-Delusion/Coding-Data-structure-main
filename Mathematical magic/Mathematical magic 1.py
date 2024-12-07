# Function to find and print the factors of a given number
def find_factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

# Get user input
number = int(input("Enter the number to find the factors: "))

# Call the function with the user input
find_factors(number) #

