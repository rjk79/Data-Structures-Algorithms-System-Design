def partition(s):
    res = []
    def isPalindrome(s):
        return s == s[::-1]
    def recurse(curr, word):
        # import pdb; pdb.set_trace()
        if word == "":
    # needed to CLONE curr
            res.append(curr[:])
            return
    # needed to go +1 on the len!!!
        for i in range(1, len(word)+1):
            start, end = word[:i], word[i:]
            if isPalindrome(start):
                curr.append(start)
                recurse(curr, end)
                curr.pop()
    recurse([], s)
    return res

print (partition("aab"))

# aab
# 1: => "a"  1: => "ab"
# 2: => "aa" 2: => "b"
# 3: => "aab"   3: => ""