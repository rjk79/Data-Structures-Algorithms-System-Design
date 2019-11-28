def originalDigits(s):
        # 11:35
# create a hash of numbers
# find the permutation of letters
# that can satisfy:
#   can be broken down into letters
#   like wordBreak
# map at end
# then sort

# _ _ _ _ _ _ _ _ _
# T _ _ _ T _ _ _ T
    dic = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
    }
#     dfs instead
    res = [None]
    def dfs(curr, cString, allCurr):
#           backt
        if len(curr) == 5 and curr not in dic: return
        if len(cString) == 0 and curr in dic and not res[0]:
            res[0] = allCurr[::] + [curr]
            print(res)
            return 
        for i in range(len(cString)):
            if curr in dic:
                dfs("" + cString[i], cString[:i] + cString[i + 1:], allCurr + [curr])
            else:
                dfs(curr + cString[i], cString[:i] + cString[i + 1:], allCurr)
    dfs("", s, [])
    res = res[0]
    newRes = []
    for el in res:
        newRes.append(dic[el])
    newRes.sort()
    return newRes

print(originalDigits("owoztneoer"))