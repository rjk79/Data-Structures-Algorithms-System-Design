def isValidSudoku(board):
    def validUnit(arr):
        arr = [el for el in arr if el != "."]
        return len(arr) == len(set(arr))
#       check rows
    for i in range(9):
        if not validUnit(board[i]): return False
#       check cols
    for i in range(9):
        zipped = zip(*board)
        if not validUnit(zipped[i]): return False
#       check boxes
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            box = [row[j:j+3] for row in board[i:i+3]]
            flattenedBox = [el for row in box for el in row]
            if not validUnit(flattenedBox): return False
    return True
                
            
grid = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(grid))