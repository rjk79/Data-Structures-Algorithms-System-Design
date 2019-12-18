def minDominoRotations(self, A, B):
    for x in [A[0],B[0]]:
        # d is a pair. check if its in every pair
        if all(x in d for d in zip(A, B)):
            return len(A) - max(A.count(x), B.count(x))
    return -1 #cant flip into valid seq

A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
print(minDominoRotations(A, B))

x = 2
[(2, 5), (1, 2), (2, 6), (4, 2), (2, 3), (2, 2)]
6 - max(4, 3) #total len - # of dom already in correct posn
