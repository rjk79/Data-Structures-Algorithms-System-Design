def sumZero(n):
    if n % 2 == 0: #even
        a= list(reversed(range(-n//2, -1+1))) + list(range(1,n//2+1))
        print(a) 
    else: #odd
        a= list(range(-n//2+1, -1+1)) + [0] + list(range(1,n//2+1))
        print(a)
sumZero(1) #0
sumZero(2) #-1 1
sumZero(3) #-2 2
sumZero(4) #-1 1
