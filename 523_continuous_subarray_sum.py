def checkSubarraySum(nums, k):
        cache = {}
        cur = 0
        for i, x in enumerate(nums):
            # record the idx + 1 where we were able to create the remainder
            if cur not in cache: cache[cur] = i
            cur = (cur + x) % k if k != 0 else cur + x
            # if we encounter the same remainder again then
            # we know we can make a multiple of 6 because 
            # there is 6 * something got us from prev num (with rem X) to curr Num (with rem X)
            if cur in cache and i > cache[cur]: 
                print(cache)

                return True
        print(cache)
        return False

# [23, 2, 4, 6, 7],  k=6

# cache = {0: 0, 5: 1, 1: 2
# cur = 0 5 1 5
# i = 0  1 2
# x = 23 2 4

# different from ^^^ (flipped 4, 6)
print(checkSubarraySum([23, 2, 6, 4, 7], 6))
print(checkSubarraySum([23, 2, 6, 4, 7], 0))
