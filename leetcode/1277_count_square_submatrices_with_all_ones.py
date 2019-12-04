# def countSquares(matrix):
# #         12:36

# # find maxLen = min(m, n) that will be longest sq length
# # count 1x1's, count 2x2's, etc until maxLen x maxLen
#     m = len(matrix)
#     n = len(matrix[0])
#     def checkArea(length, point):
#         i, j = point
#         if point == [0, 3]:
#             import pdb;pdb.set_trace()
#         for x in range(length):
#             for y in range(length):
#                 xi, yj = x + i, y + j
#                 if not (0 <= xi < m and 0 <= yj < n):
#                     return False
#                 if matrix[xi][yj] != 1:
#                     return False
#         return True
    
#     count = 0
#     maxLen = min(m, n)
#     for length in range(0, maxLen):
#         for i in range(m):
#             for j in range(n):  
#                 if matrix[i][j] != 0 and checkArea(length, [i, j]):
#                     count += 1
#     return count

def countSquares(matrix):
#         12:36

# find maxLen = min(m, n) that will be longest sq length
# count 1x1's, count 2x2's, etc until maxLen x maxLen
    m = len(matrix)
    n = len(matrix[0])
    def checkArea(length, point):
        i, j = point
        # if point == [1, 2]:
            # import pdb;pdb.set_trace()
        # left and up and leftup
        dirs = [[0, -1], [-1, 0], [-1, -1]]
        for x, y in dirs:
                xi, yj = x + i, y + j
                if not (0 <= xi < m and 0 <= yj < n):
                    return False
                if matrix[xi][yj] < length: # 1 2     1
                    return False
        matrix[xi][yj] = length + 1
        return True
    
    count = 0
    maxLen = min(m, n)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1: count += 1
    # dist away from point we need to check
    for length in range(0, maxLen + 1):
        for i in range(1, m):
            for j in range(1, n):  
                if matrix[i][j] == length and checkArea(length, [i, j]):
                    # print(i, j, length)
                    count += 1
    print(matrix)
    return count

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

# 0 1 1 1 
# 1 1 2 2 
# 0 2 2 2 

print(countSquares(matrix)) #15