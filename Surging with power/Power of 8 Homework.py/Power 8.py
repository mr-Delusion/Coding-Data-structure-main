def power8(f):
    if f <= 0:
        return False
    return (f & (f - 1)) == 0 and (f & 0b11111111) == f
try:
    input = int(input("Enter a number to check if it is a power of 8: "))
    if power8(input):
        print(f"{input} is a power of 8.")
    else:
        print(f"{input} is not a power of 8.")
except ValueError:
    print("Please enter a valid integer.")
