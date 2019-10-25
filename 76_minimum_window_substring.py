import collections
def minWindow(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
#       T fits inside S
        tCounts = collections.Counter(t)
        sCounts = collections.Counter(s)
        l = 0
        r = len(s) - 1
        while l < r:
            leftChar = s[l]
            rightChar = s[r]
            if leftChar in tCounts and rightChar in tCounts and tCounts[leftChar] == sCounts[leftChar] and tCounts[rightChar] == sCounts[rightChar]:
                break
            if leftChar in tCounts and sCounts[leftChar] > tCounts[leftChar]:
                sCounts[leftChar] -=1
                l += 1
            elif leftChar not in tCounts:
                l += 1
            if rightChar in tCounts and sCounts[rightChar] > tCounts[rightChar]:
                sCounts[rightChar] -= 1
                r -= 1
            elif rightChar not in tCounts:
                r -= 1
            print (leftChar, rightChar, tCounts, sCounts)
            
        return s[l:r+1]
#   create Counter hash O(n)
#   have 2 pointers at both ends
#   pinch both in as long they dont reduce a count below 1
#   return the pointers' idxs when they both cant move

print (minWindow("ADOBECODEBANC", "ABC")) #BANC