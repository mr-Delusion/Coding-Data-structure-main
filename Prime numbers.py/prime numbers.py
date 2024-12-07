from math import sqrt
number = int(input("Enter the number to check: "))

if number > 1:
    for x in range(2, int(sqrt(number))+1):
        if(number % x) == 0:
            print("This is not a prime number!")
            break
        else:
            print("This is a prime number!")    