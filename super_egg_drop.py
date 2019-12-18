def superEggDrop(K, N):
    dp = [[0] * (K + 1) for i in range(N + 1)]
    for m in range(1, N + 1):
        for k in range(1, K + 1):
            dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
        if dp[m][K] >= N: 
            for line in dp:
                print(line)
            return m

# print(superEggDrop(1, 2))
# print(superEggDrop(2, 6))
# print(superEggDrop(3, 14))
print(superEggDrop(3, 14))