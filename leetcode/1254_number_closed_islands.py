
def closedIsland(grid):
#   iter every sq
#       run a dfs on the sq
#       if you encounter go out of bounds then ret -inf
# easier =>
# iter thru boundaries and mark as 1s
    DIRS = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    m = len(grid)
    n = len(grid[0])
    count = 0
    
    def dfs(point):
        i, j = point
        grid[i][j] = 1
        for x, y in DIRS:
            xi, yj = i + x, y + j
            if 0 <= xi < m and 0 <= yj < n:
                if grid[xi][yj] == 0:
                    dfs([xi, yj])
#       top and bottom border
    for j in range(n):
        if grid[0][j] == 0:
            dfs([0, j])
            # dont use -1 => it will mess up dirs
        if grid[m-1][j] == 0:
            dfs([m-1, j])
#       left and right border

    for i in range(m):
        if grid[i][0] == 0: 
            dfs([i, 0])
            # dont use -1 => it will mess up dirs
        if grid[i][n - 1] == 0:
            dfs([i, n-1])

    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                count += 1
                dfs([i, j])
    return count
                
a = [[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]
print(closedIsland(a))