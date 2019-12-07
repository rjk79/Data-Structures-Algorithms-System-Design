def optim(arr):
    n = len(arr)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[j - 1] > arr[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1 #leftup + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) #max of left and up
    return dp[-1][-1]



arr = [5, 8, 3, 7, 9, 1]
print(optim(arr))