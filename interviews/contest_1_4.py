def freqAlphabets(s):
    dic = dict()
    for i in range(1,27):
        if i < 10:
            dic[str(i)] = chr(i + 96)
        else:
            dic[str(i)+"#"] = chr(i + 96)

    res = []
    def dfs(start, curr):
        print(curr, start)
        if start == len(s):
            res.append(curr)
        for end in range(start, len(s)+1):
            if s[start:end] in dic:
                dfs(end, curr + dic[s[start:end]])
    dfs(0, "")
    print(res)
    return "".join(res[0])

# print(freqAlphabets("10#11#12"))
def xorQueries(arr, queries):
    res = []
    for query in queries:
        curr = arr[query[0]]
        for i in range(query[0] + 1, query[1]+1): #
            print(i, arr[i])
            curr ^= arr[i]
        res.append(curr)
    return res
a = [1,3,4,8]
b = [[0,1],[1,2],[0,3],[3,3]]
# [2,7,14,8] 
print(xorQueries(a, b))