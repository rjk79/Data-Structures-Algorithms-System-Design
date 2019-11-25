def numRookCaptures(board):
#    R white rook
#    . empty
#    B white bishop
#    p black pawn
#     
# define dirs
# add a dir to the rooks posn until we hit end of board or B or p 
# if we stop on a pawn count += 1
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "R":
                    init = [i, j]
        count = 0
        DIRS = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for x, y in DIRS:
            xi, yj = init
            while True:
                xi, yj = xi + x, yj + y
#               if not in bounds or its a bishop
          
                if not (0 <= xi < m and 0 <= yj < n) or board[xi][yj] == "B":
                    break
                elif board[xi][yj] == "p":
                    count += 1
                    break
        return count

a = [[".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","R",".",".",".","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."]]
print(numRookCaptures(a))                