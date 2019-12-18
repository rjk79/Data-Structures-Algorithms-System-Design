import collections
def checkInclusion(s1, s2):
        s1Counts = collections.Counter(s1)
        s2Counts = collections.defaultdict(int)
        start = 0
        matchCount = 0
        for end in range(len(s2)):
            char = s2[end]
            s2Counts[char] += 1
            if s2Counts[char] > s1Counts[char]:
                    matchCount -= 1
            if len(s2Counts) > len(s1Counts):
                startChar = s2[start]
                s2Counts[startChar] -= 1
                if s2Counts[startChar] < s1Counts[startChar]:
                    matchCount -= 1
                if s2Counts[startChar] == 0:
                    del s2Counts[startChar]
                start += 1
            
            if char in s1Counts and s2Counts[char] == s1Counts[char]:
                matchCount += 1

            if matchCount == len(s1Counts): 
                return True
            print(matchCount)
        return False

print(checkInclusion("hello", "ooolleoooleh")) #False
# 1 0 0

print(checkInclusion("ab", "eidbaooo")) #True


