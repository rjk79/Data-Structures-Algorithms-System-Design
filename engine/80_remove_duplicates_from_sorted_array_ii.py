def removeDuplicates(self, nums):
    i = 0
    for n in nums:
        # if its greater than the thing 2 to the left
        # or if we're just working on the 1st 2 els in our arr
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
        # things that dont conditional are skipped (dups that would exceend 2nd dup)
        # "i" is how far we get mutating our input
    return i

# [0,0,1,1,1,1,2,3,3]
#  0 0 1 1 2 3 3
# i = 0 1 2 3 4 5 6
# n = 0 0 1 1 1 1 2 3 3