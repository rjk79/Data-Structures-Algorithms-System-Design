import collections
def anagramDiff(str1, str2):
    res = 0
    aCount = collections.Counter(str1)
    bCount = collections.Counter(str2)
    for char in aCount.keys():
        if char in bCount.keys():
            if aCount[char] > bCount[char]:
                res += abs(aCount[char] - bCount[char])
        else:
            res += aCount[char]
    return res

print (anagramDiff("abb", "abc")) #1

# lack of something thats in str2 
# and presence of something not in str2 are not mutually exclusive
# e.g. str1 might not have enough "b"s because it has an extra "c"
print (anagramDiff("dbc", "abb")) #2

print (anagramDiff("bbcc", "bbbc")) #1
print (anagramDiff("bcc", "bbc")) #1