import collections
def minCostToMoveChips(chips):
    res = 0
    counts = collections.Counter(chips).items()
#       # of things at each posn
    for count in counts:
        if count[0] % 2 != 0:
            res += count[1]
    return res

print(minCostToMoveChips([1,2,3]))
print(minCostToMoveChips([2,2,2,3,3]))