# values = [60, 100, 120]
# weights = [10, 20, 30]
# 50

# 220

# DFS, greedy, dp
# weights for idx, total values for elems
# [0, 1, 2, 3, 10...20...30...40...50]
# [0, 0, 0, 0, 60   100  160  180  220]
# 


# a row num = the range of items we are considering
# col num = the weight we are trying to fill
def knapsack(vals, wts, W):
    dp = [[0 for _ in range(W + 1)] for _ in range(len(vals) + 1)]
    for i in range(len(dp)):
        for w in range(len(dp[0])):
            if i == 0 or w == 0:
                dp[i][w] = 0
            # if curr item's wt is too large, we cant consider it for this curr wt
            # so just refer to val above ()
            elif wts[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # max of: best val while not considering the curr item and 
                # val of curr item + best while not considering the curr item at the remaining weight
                dp[i][w] = max(vals[i-1] + dp[i - 1][w - wts[i - 1]], dp[i - 1][w])
    return dp[-1][-1]

print (knapsack([60, 100, 120], [10, 20, 30], 50))