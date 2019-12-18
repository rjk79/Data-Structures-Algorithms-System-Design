def maxAreaOfIsland(grid):
    DIRS = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    m = len(grid)
    n = len(grid[0])
    counts = []

    def dfs(point):
        count = 1
        i, j = point
        grid[i][j] = 0
        for x, y in DIRS:
            xi, yj = i + x, y + j
            if 0 <= xi < m and 0 <= yj < n:
                if grid[xi][yj] == 1:
                    count += dfs([xi, yj]) 
        return count
#       top and bottom border
    for j in range(n):
        if grid[0][j] == 1:
            dfs([0, j])
        if grid[m-1][j] == 1:
            dfs([m-1, j])
#       left and right border
    for i in range(m):
        if grid[i][0] == 1: 
            dfs([i, 0])
        if grid[i][n-1] == 1:
            dfs([i, n-1])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                res = dfs([i, j])
                # print(res)
                counts.append(res)
    return max(counts)

a = 
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(a)) #6