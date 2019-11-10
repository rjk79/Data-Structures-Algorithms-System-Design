def oddCells(n, m, indices):
    res = [[0 for _ in range(m)] for _ in range(n)]
    for ri, ci in indices:
        for row in range(n):
            res[row][ci] += 1
        for col in range(m):
            res[ri][col] += 1
    count = 0
    for i in range(n):
        for j in range(m):
            if res[i][j] % 2 != 0: count += 1
    return count
n = 2
m = 3
indices = [[0,1],[1,1]]
print(oddCells(n, m, indices))

n = 2
m = 2
indices = [[1,1],[0,0]]
print(oddCells(n, m, indices))

n = 1
m = 1
indices = [[0, 0], [0, 0]]
print(oddCells(n, m, indices))

