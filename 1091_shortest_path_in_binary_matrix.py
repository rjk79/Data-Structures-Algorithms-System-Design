def shortestPathBinaryMatrix(grid):
# 5:21 start
# 5:29 naive
    m = len(grid)
    n = len(grid[0])
    best = []
    dp = [[0 for _ in range(n)] for m in range(m)]
    def dfs(point, curr, visited):
        
        if point == [m - 1, n - 1]: 
            best.append(curr)
            return 0
        visited.add(str(point))
        i, j = point
        if dp[i][j]: 
            best.append(curr)
            return dp[i][j]
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        dists = []
        for x, y in dirs:
            xi, yj = x + i, y + j
            if 0 <= xi < m and 0 <= yj < n:
                # import pdb;pdb.set_trace()
                if grid[xi][yj] == 0 and str([xi, yj]) not in visited:
                    dists.append(dfs([xi, yj], curr + 1, visited))
        visited.remove(str(point))
        dp[i][j] = 1 + min(dists)
        return dp[i][j]
    dfs([0, 0], 1, set())
    import pdb;pdb.set_trace()

    return min(best)
print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])) # 4

# 0 0 0
# 1 1 0
# 1 1 0

# 