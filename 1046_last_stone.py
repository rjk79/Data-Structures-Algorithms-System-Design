def lastStoneWeight(stones):
#   compare largest until one remains
    stones.sort()
    while len(stones) > 1:
        biggest = stones.pop()
        second = stones.pop()
        if biggest != second:
            stones.append(max([biggest, second]) - min([biggest, second]))
    return stones[0] if stones else None
print (lastStoneWeight([2,7,4,1,8,1]))