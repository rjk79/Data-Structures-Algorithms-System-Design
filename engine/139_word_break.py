        
def wordBreak(s, wordDict):

    dp = [False] * len(s)
    for i in range(len(dp)):
        for word in wordDict:
#            i = 7, word = "leet" with len = 4, s[4:8]
#            i = 7, other word ends right before we start at [3]
#            "or ..." allows us to start the string (i = 3, len(word) = 4)
            # first check only fails on first few iterations, need the +1's because it's 0 indexed
            if s[i - len(word) + 1:i + 1] and (dp[i - len(word)] or i - len(word) == -1):
                dp[i] = True
    print(dp)
    return dp[-1]

print(wordBreak("leetcode", ["leet","code"]))