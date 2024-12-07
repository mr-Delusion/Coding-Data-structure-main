
def poweroftwo (n):
    if (n == 0):
        return False
    else:
        while (n % 2 == 0):
            n = n/2
    return (n == 1)   
print(poweroftwo(8))
# print (bin(14))