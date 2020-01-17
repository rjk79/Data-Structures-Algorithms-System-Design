def solveNQueens(n):
    res = []
#  [ [], [], []]
    def recurse(cols, sums, diffs):
        print(cols, sums, diffs)
#           use col as a proxy for iter count
        row = len(cols)
        if row == n:
            res.append(cols)
            return
        for col in range(n): #
            if (col not in cols) and (row - col not in diffs) and (row + col not in sums):
#   use + so arrs arent mutated (backtracking)
                recurse(cols+[col], sums+[row + col], diffs+[row - col])
    recurse([], [], [])
    return [["." * i + "Q" + "." * (n - i - 1) for i in cols] for cols in res]
# 0,0
#    1,1    3,1
#       Q
#    1,3    3,3
# 
# to check for diagonals
# x,y is where a queen is
# x2 + y2 != x + y  pos slope diags
#    -         -    neg 

for row in solveNQueens(4):
    print(row)