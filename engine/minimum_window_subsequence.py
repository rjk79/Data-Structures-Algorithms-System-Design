# def minWindowSubseq(S, T):
    #  a b c d e b d d e
    #  0 0 0 0 0 0 0 0 0
    # b  1       1
    # d      2     2 2
    # e        3       3
    

def recurse(S, T):
    res = []
    def dfs(origStart, start, tIdx):
        print((origStart, start, tIdx))
        if tIdx == len(T):
            res.append(start - origStart+1)
            return #prevents idxing out
        for end in range(start, len(S)):
            if S[end] == T[tIdx]:
                dfs(origStart, end+1, tIdx+1)

    for origStart in range(len(S)):
        dfs(origStart, 0, 0)
    return res
S = "abcdebdde"
T = "bde"
#4
print(recurse(S, T))
