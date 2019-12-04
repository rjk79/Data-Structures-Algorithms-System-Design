def generateMatrix(n):
    A, lo = [], n*n+1
    while lo > 1:
        import pdb; pdb.set_trace()
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A
print(generateMatrix(3))