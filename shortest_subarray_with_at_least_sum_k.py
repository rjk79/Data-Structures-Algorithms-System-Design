import collections
def shortestSubarray(A, K):
    q = collections.deque([[0, 0]])
    res, cur = float('inf'), 0
    for i, a in enumerate(A):
        cur += a
        # 1st thing in q's sum
        while q and cur - q[0][1] >= K: 
            res = min(res, i + 1 - q.popleft()[0])
        # last thing in q's sum
        while q and cur <= q[-1][1]:
            q.pop()
        # index, best sum
        q.append([i + 1, cur])
        import pdb;pdb.set_trace()
    return res if res < float('inf') else -1

a = [84,-37,32,40,95]
b = 167
print(shortestSubarray(a, b))
# [2, 47] [1, 84] [0, 0]
# q = [[3, 79]
# res = inf 4
# cur = 0 84 47 79 119
# i 0 1 2 3
# a 