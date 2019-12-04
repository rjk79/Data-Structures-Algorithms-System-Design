import collections
def lengthOfLongestSubstring(s):
        best = 0
        for i in range(len(s)):
            counts = collections.defaultdict(int)
            for j in range(i, len(s)):
                counts[s[j]] += 1

                if counts[s[j]] > 1: 
                    
                    break
                    # + 1 and - 1 cancel out. - because we overshot and + to adj for idxes
            if j - i  > best: best = j - i 
        return best
print (lengthOfLongestSubstring("abcabcbb"))