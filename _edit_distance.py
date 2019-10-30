# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# completed using Recurs, Memo

def minDistance(self, word1, word2):
    dp = [[float('inf') for _ range(len(word2))] for _ in range(len(word1))]
    for i in range(len(dp)):
        dp[i][0] = i
    for j in range(len(dp[0])):
        dp[0][j] = j
    

    

def minDistance(self, word1, word2):
        # """Naive recursive solution"""
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            # move on to the next letter
            return self.minDistance(word1[1:], word2[1:])
        # pretends we insert something so move on to next letter in target word
        insert = 1 + self.minDistance(word1, word2[1:])
        # move on next letter in curr word
        delete = 1 + self.minDistance(word1[1:], word2)
        # both move up by 1
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)

# taking from top-left diag is replacing
# taking from left is insert
# taking from above is delete
#      S  O  R
#   0  1  2  3 
# E 1  1  2  3
# S 2
# R 3
# O 4
# H 5

# 1,1 replace
# 1,2 replace>insert or insert>replace
# 1,3 replace>insert>insert


def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    # table[i-1] (going up) would be the equiv of deleting a char out of word2
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]

    