import collections

def max_distance(grid):
    # m is rows, n is cols
    m = len(grid)
    n = len(grid[0])

    # edge: if grid has nothing or grid is a 1 x 1 square (=1)
    if grid == [] or m * n == 1: return -1

    q = collections.deque([ [i, j] for i in range(m) for j in range(n) if grid[i][j] == 1 ])

    currMax = 0
    dirs = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]

    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for x, y in dirs:
                xi, yj = x + i, y + j
                # if we havent visited it before and its a water space
                if xi < m and yj < n and grid[xi][yj] == 0:
                    q.append([xi, yj])
                    grid[xi][yj] = 1
        currMax += 1
    return currMax - 1

print max_distance([[1, 0, 1], [0, 0, 0], [1,0, 1]])

