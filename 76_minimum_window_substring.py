def minWindow(s, t):
       
    chars = {}  # stores the character and their count in t
    for i in t:
        chars[i] = chars.get(i, 0) + 1
        
    dic = {}    # stores the character and their count in s
    l, r = 0, 0
    res, length = "", len(s) + 1
    valid = 0 
    
    while(r < len(s)):
        if s[r] in chars:
            dic[s[r]] = dic.get(s[r], 0) + 1
            if chars[s[r]] == dic[s[r]]:
                valid += 1
        r += 1
        
        if valid == len(chars):   # the substring s[l:r] contains all the character in t
            while(valid == len(chars)): 
                if s[l] in chars:
                    dic[s[l]] -= 1
                    if dic[s[l]] < chars[s[l]]: # if the substring is not valid, stop looping
                        if dic[s[l]] == 0:
                            del dic[s[l]]
                        valid -= 1
                l += 1
            if r - l + 1 < length:
                length = r - l + 1
                res = s[l - 1:r]
                print(res)
                
    return res
# import collections
# def minWindow(s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
# #       T fits inside S
#         tCounts = collections.Counter(t)
#         sCounts = collections.Counter(s)
#         l = 0
#         r = len(s) - 1
#         while l < r:
#             leftChar = s[l]
#             rightChar = s[r]
#             if leftChar in tCounts and rightChar in tCounts and tCounts[leftChar] == sCounts[leftChar] and tCounts[rightChar] == sCounts[rightChar]:
#                 break
#             if leftChar in tCounts and sCounts[leftChar] > tCounts[leftChar]:
#                 sCounts[leftChar] -=1
#                 l += 1
#             elif leftChar not in tCounts:
#                 l += 1
#             if rightChar in tCounts and sCounts[rightChar] > tCounts[rightChar]:
#                 sCounts[rightChar] -= 1
#                 r -= 1
#             elif rightChar not in tCounts:
#                 r -= 1
#             print (leftChar, rightChar, tCounts, sCounts)
            
#         return s[l:r+1]
#   create Counter hash O(n)
#   have 2 pointers at both ends
#   pinch both in as long they dont reduce a count below 1
#   return the pointers' idxs when they both cant move

print (minWindow("ADOBECODEBANC", "ABC")) #BANC

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
