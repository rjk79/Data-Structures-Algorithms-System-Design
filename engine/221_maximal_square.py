def maximalSquare(matrix):
    if not matrix: return 0
    m , n = len(matrix), len(matrix[0])
    dp = [[ 0 if matrix[i][j] == 0 else 1 for j in range(0, n)] for i in range(0, m)]
    # start at 1 for each range to avoid going out of bounds
    for i in range(1, m):
        for j in range(1, n):
            # if its a 1 itself
            if matrix[i][j] == 1:
            # look UP, LEFT, UPLEFT. lowest one is limiting (prevents a larger sq from being made)
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = 0
    
    res = max(max(row) for row in dp)
    print(dp)
    return res ** 2

print(maximalSquare([[1, 0, 1, 0, 0], 
                    [1, 0, 1, 1, 1], 
                    [1, 1, 1, 1, 1], 
                    [1, 0, 0, 1, 0]]))