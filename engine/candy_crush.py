def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        temp = list(map(list, [*zip(*reversed(board))])) #reverse then zip
        m = len(temp)
        n = len(temp[0])
        while True:
            toCrush = set()
            for i in range(2, m):
                for j in range(n):
#                   0's dont count as matches. find triplets
                    if temp[i][j] and temp[i][j] == temp[i-1][j] and temp[i][j] == temp[i-2][j]:
                        toCrush |= {(i,j), (i-1,j), (i-2,j)} 
            for i in range(m):
                for j in range(2, n):
                    if temp[i][j] and temp[i][j] == temp[i][j-1] and temp[i][j] == temp[i][j-2]:
                        toCrush |= {(i,j), (i,j-1), (i,j-2)}
            if not len(toCrush): break #nothing to crush

            for x, y in toCrush: temp[x][y] = 0

            temp = [list(filter(lambda a: a != 0, row)) for row in temp]
            temp = [row + [0] * (n - len(row)) for row in temp] 
            # print(temp)
        board = [list(row) for row in [*zip(*temp)]] #zip then reverse
        board.reverse()
        return board

# rotate array
# then look for triplets
# set called Crushed
# unrotate
            
            
        
# 210
# 310
# 410
# 5
# 610
# 710
# 810
# 1
# 4
#       R-side, reading downward: 110 5