# def longestIncreasingPath(self, matrix):
       
#         if not matrix: return 0
#         self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
#         m = len(matrix)
#         n = len(matrix[0])
#         cache = [[-1 for _ in range(n)] for _ in range(m)]
#         res = 0

#         for i in range(m):
#             for j in range(n):
#                 # always comp to best
#                 cur_len = self.dfs(i, j, matrix, cache, m, n)
#                 res = max(res, cur_len)
#         return res
        
#     def dfs(self, i, j, matrix, cache, m, n):
#         # if we have a memo return it
#         if cache[i][j] != -1:
#             return cache[i][j]
#         res = 1
#         for direction in self.directions:
#             x, y = i + direction[0], j + direction[1]
#             if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
#                 continue
#             length = 1 + self.dfs(x, y, matrix, cache, m, n)
#             # update res if we found a longer path
#             res = max(length, res)
#         # save the longest path we found
#         cache[i][j] = res
#         return res




def longestIncreasingPath(matrix):
#        2 dp arrays (not really dp)
#  if somethign is not marked as possible (1) and its a higher val, go to it by running DFS
#         find overlaps between 2 dp arrs
    if not matrix: return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    res = []

    def dfs(point):
        i, j = point
        if dp[i][j]: return dp[i][j]
        best = 1
        for x, y in dirs:
            xi, yj = x + i, y + j
            if 0 <= xi < m and 0 <= yj < n and matrix[xi][yj] > matrix[i][j]:
                best = max(best, 1 + dfs([xi, yj]))
        # base returns 1
        dp[i][j] = best    
        return best

    for i in range(m):
        for j in range(n):
            res.append(dfs([i, j]))
    print(dp)
    return max(res)

print (longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])) #4
# dp = [[4, 3, 2], [1, 4, 1], [2, 1, 2]]
print (longestIncreasingPath([[7,8 ,9],[9,7 ,6],[7,2 ,3]])) #6
# dp = [[3, 2, 1], [1, 3, 4], [2, 6, 5]]
print (longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])) #4
# dp = [[1, 1, 2], [2, 2, 1], [3, 4, 2]]
# print (longestIncreasingPath([[18,1,12,16,5,18,14,14,6,4,9,4,4,5,3,9,9,12,18,2,19,4,5,14,16,6,15,8,9,0],[9,10,11,15,15,8,2,17,17,2,0,18,8,14,19,8,1,2,3,1,19,6,13,16,0,15,0,17,13,1],[13,11,15,6,4,8,3,8,19,0,7,4,3,2,15,10,2,9,18,7,10,2,0,17,5,4,13,1,10,4],[5,9,12,11,4,9,19,15,2,13,3,17,7,2,5,18,17,7,9,15,10,15,2,12,2,10,14,18,2,4],[14,6,18,5,18,10,18,5,9,13,7,15,11,6,18,4,12,17,18,15,1,4,15,13,19,11,11,1,13,7],[8,16,12,4,9,12,17,5,10,4,2,5,11,2,6,0,0,16,14,0,3,19,10,19,7,14,2,1,18,4],[17,3,3,5,0,16,13,3,4,4,15,1,14,11,12,9,8,3,13,15,17,18,11,2,15,3,3,19,1,12],[0,1,11,7,7,4,10,14,2,6,5,11,11,0,18,8,12,13,6,3,5,6,8,0,2,6,5,18,3,17],[13,16,18,8,19,9,19,0,18,16,16,5,0,2,16,9,4,7,11,13,8,16,7,4,10,17,0,0,19,18],[19,14,14,16,17,7,8,17,8,16,12,8,4,19,14,5,19,4,5,5,19,7,17,18,8,0,5,5,18,11],[18,8,6,16,13,0,13,8,18,17,14,14,9,10,16,0,3,15,0,9,6,9,2,8,6,13,4,4,12,5],[15,4,1,12,1,6,12,17,16,11,14,4,5,9,11,17,15,6,14,18,3,5,17,19,19,7,7,1,7,8],[14,16,19,11,5,6,0,0,13,2,8,10,8,10,13,2,19,5,6,15,15,4,3,6,3,16,18,18,18,5],[16,6,17]]))


# [3, 4, 5]
# [3, 2, 6]
# [2, 2, 1]
# 4 

# [8, 9]
# [7, 6]
# [2, 3]

# [0 ,1]


# [3, 2, 1]
# [1, 3, 4]
# [2, 6, 5]

# 7 8 9
# 9 7 6
# 7 2 3 

# [0, 2] []



# [[9,9,4],[6,6,8],[2,1,1]] => 4    
# [[7,8 ,9],[9,7 ,6],[7,2 ,3]] => 6
# [[3,4,5],[3,2,6],[2,2,1]] => 4