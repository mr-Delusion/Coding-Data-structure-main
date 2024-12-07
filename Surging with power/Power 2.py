def power2(n):
    if n <= 0:
        return False
    else:
        return (n & (~(n-1))) == n
print(power2(8))    
