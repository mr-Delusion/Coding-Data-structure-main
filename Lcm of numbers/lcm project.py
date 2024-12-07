def gcd(a, b):
    """Calculate the greatest common divisor using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate the least common multiple."""
    return abs(a * b) // gcd(a, b)

def main():
    print("Welcome to the LCM Calculator!")
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if num1 <= 0 or num2 <= 0:
            print("Please enter positive integers.")
            return

        result = lcm(num1, num2)
        print(f"The least common multiple of {num1} and {num2} is: {result}")
    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()
