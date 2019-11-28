import itertools
def canPartition(nums):
    perms = itertools.permutations(nums, len(nums))
    perms = [list(perm) for perm in perms]

    for perm in perms:   
        perm = list(perm)
        l = 0
        r = len(perm)
        while l <= r:
            mid = (l + r) //2
            leftSum = sum(perm[:mid])
            rightSum = sum(perm[mid:])
            if leftSum > rightSum:
                r = mid - 1
            elif leftSum < rightSum:
                l = mid + 1
            else:
                return True
    return False
print(canPartition([1, 5, 5, 11]))
    