import collections
import itertools

def totalHammingDistance(nums):
    
    def hammingDistance(num1, num2):
        return (collections.Counter(bin(num1 ^ num2)[2:])["1"])

    pairs = itertools.combinations(nums, 2)

    count = 0
    for x, y in pairs:
        count += hammingDistance(x, y)
    
    return count

print (totalHammingDistance([3, 4, 2]))
# 011
# 100

# 2, 4, 14:

# 2, 4
# 2, 14
# 4, 14