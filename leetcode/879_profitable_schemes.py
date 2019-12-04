
            
def profitableSchemes(G, P, group, profit):
       
        dp = [[0] * (G + 1) for _ in range(P + 1)]
        dp[0][0] = 1
        
        for g0, p0 in zip(group, profit):
            # need to make deep copy
            dpClone = [row[:] for row in dp]
            for p1 in range(len(dp)):
#               e.g. 5 - 2 = 3 -> 0, 1, 2, 3
                p2 = min(p0 + p1, P)
                for g1 in range(G - g0 + 1):
                    g2 = g0 + g1
# the num of ways we can get this profit with this number of mems is the num of ways we can the previous profits/nums of mems
                    dpClone[p2][g2] += dp[p1][g1]
                    dpClone[p2][g2] %= 10**9 + 7
            dp = dpClone
#       total ways we can get our target profit
        return sum(dp[-1]) % 10**9 + 7

print (profitableSchemes(5, 3, [2, 2], [2, 3]))
print (profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))

#           Gang mems
#       [[1, 0, 0, 0, 0, 0], 
#profit [0, 0, 0, 0, 0, 0], 
#       [0, 0, 1, 0, 0, 0], 
#       [0, 0, 0, 0, 0, 0]]
# 
# 0, 0    2, 2


# [[1, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0], 
# [0, 0, 1, 0, 0, 0], 
# [0, 0, 1, 0, 1, 0]]


# POINT AT 3, 2             POINT AT 3, 4
# p0 3                      .
# g0 2                      .
# p1 0 (only 1 in 1st row)  2 (only 1 in 3rd row)
# p2 3                      3
# g1 0 (g2 - g0)            2 (g2 - g0)
# g2 2                      4

# 