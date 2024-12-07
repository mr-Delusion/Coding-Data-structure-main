def binary_to_decimal(binary_str):
    """Convert binary string to decimal integer."""
    try:
        decimal = int(binary_str, 2)
        return decimal
    except ValueError:
        return "Invalid binary input."

def decimal_to_binary(decimal):
    """Convert decimal integer to binary string."""
    try:
        binary = bin(decimal)[2:]  # Remove '0b' prefix
        return binary
    except TypeError:
        return "Invalid decimal input."
    
print("Choose an option:")
print("1. Convert Binary to Decimal")
print("2. Convert Decimal to Binary")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    binary_input = input("Enter a binary number: ")
    result = binary_to_decimal(binary_input)
    print("Decimal representation:", result)
elif choice == "2":
    decimal_input = input("Enter a decimal number: ")
    try:
        decimal_number = int(decimal_input)
        result = decimal_to_binary(decimal_number)
        print("Binary representation:", result)
    except ValueError:
        print("Invalid decimal input.")
else:
    print("Invalid choice.")
