def setZeroes(matrix):
      
        firstCol = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0: firstCol = True
            # if you start at col 0, then setting matrix[0][0] to 0 will cause 1st row to be changed
            # even though you only wanted the 1st col to change
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in reversed(range(0, len(matrix))):
            for j in reversed(range(1, len(matrix[0]))):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            # if this line came before "for loop", would make 1st thing in every row 0 (explains why outside FOR loop)
            # in order to prevent this, we need to change 1st col LAST

            # need to set top row last for same reason (explains REVERSED)
            if firstCol: matrix[i][0] = 0

            # 


grid = [[1,1,1],[1,0,1],[1,1,1]]

#  x ------> v
#  x ------> v
#  x ------>

#  x <------
#  x <------ ^
#  x <------ ^

# 1 1 1   =>  0 1 1 =>  0 
# 0 1 2       0 1 2     0 0 0


# 0 1 1
# 0 0 0


# 1 1 1
# 1 0 1
# 1 1 1

# 1 0 1
# 0 0 0 
# 1 0 1
setZeroes(grid)
print (grid)