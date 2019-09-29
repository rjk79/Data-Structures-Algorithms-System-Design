# Input: 2.10000, 3
# Output: 9.26100

def myPow(x, n):
    if n > 0:
        return x * myPow(x, n - 1)
    elif n < 0:
        return 1/x * myPow(x, n + 1)
    else:
        return 1

print( myPow(2.00000, 10))
print (myPow(2.1000, 3))
print (myPow(2.00000, -2))