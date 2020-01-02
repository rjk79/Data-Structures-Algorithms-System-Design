def updateBoard(board, click):
# M   u mine
# E   u 0
# B   r 0
# 1-8 r
# X   r mine
    m = len(board) # num of rows
    n = len(board[0]) # num of cols
    dirs = [[0, 1], [1, 0], [-1, 1], [1, -1], [-1, 0], [0, -1], [1, 1], [-1, -1]]
    def dfs(posn):
        i, j = posn
        count = 0 # num of mines adjacent
        toVisit = []
        for x, y in dirs:
            xi, yj = x + i, y + j
            if 0 <= xi < m and 0 <= yj < n:
                if board[xi][yj] == 'E':
                    toVisit.append([xi, yj])
                elif board[xi][yj] == 'M':        
                    count += 1
        if count != 0:
            board[i][j] = count # 1-8
        else:
            board[i][j] = 'B'   # 0
            for next in toVisit:
                dfs(next)
    i, j = click    
    if board[i][j] == 'M':
        board[i][j] = 'X' # X
        return board
    else:
        dfs(click)
    return board
# EXAMPLE 1
a = [['B', '1', 'E', '1', 'B'],
    ['B', '1', 'M', '1', 'B'],
    ['B', '1', '1', '1', 'B'],
    ['B', 'B', 'B', 'B', 'B']]
b = [1,2]

# c = [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# print(updateBoard(a, b))

# EXAMPLE 2
a = [['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'M', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E']]
b = [3,0]

# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]

print(updateBoard(a, b))
