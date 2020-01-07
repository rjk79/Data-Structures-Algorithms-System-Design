# def isInterleave1(s1, s2, s3):
#     r, c, l= len(s1), len(s2), len(s3)
#     if r+c != l:
#         return False
#     dp = [[True for _ in xrange(c+1)] for _ in xrange(r+1)]
#     for i in xrange(1, r+1):
#         dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
#     for j in xrange(1, c+1):
#         dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
#     for i in xrange(1, r+1):
#         for j in xrange(1, c+1):
#             dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
#                (dp[i][j-1] and s2[j-1] == s3[i-1+j])
#     for row in dp:
#         print(row)
#     return dp[-1][-1]

def isInterleave(s1, s2, s3):
    m = len(s1)
    n = len(s2)
    dp = [[False for _ in range(n+1)] for _ in range(m+1)] #offset
    dp[0][0] = True
    for j in range(1,n): #1st row
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    for i in range(1,m): #1st col
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            # as we go down/across, idx in s3 incs
            resumeS1 = dp[i][j-1] and s2[j-1] == s3[i+j-1] #left
            resumeS2 = dp[i-1][j] and s1[i-1] == s3[i+j-1] #up
            dp[i][j] = resumeS1 or resumeS2
    # for row in dp:
    #     print(row)
    return dp[-1][-1]

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
# print(isInterleave1(s1, s2, s3))
print(isInterleave(s1, s2, s3))
