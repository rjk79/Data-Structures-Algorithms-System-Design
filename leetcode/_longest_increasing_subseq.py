def lengthOfLIS(nums):
    res = [float('-inf')]
    for num in nums:
        if num > res[-1]:
            res.append(num)
        elif num < res[-1] and len(res) > 1:

            res.append(num)
            # swap down until the thing to the left is less 
            i = len(res) - 1
            # swap past if theyre == also. so that i --
            while i > 0 and res[i] <= res[i - 1]:
                res[i], res[i - 1] = res[i - 1], res[i]
                i -= 1
            # import pdb; pdb.set_trace()

            res.pop(i + 1)
    return len(res) - 1

# [0, 10, 9]
# i = 2
# i = 1
# i = 2

print (lengthOfLIS([10,9,2,5,3,7,101,18])) #4
print (lengthOfLIS([4,10,4,3,8,9])) #3

# whenever u encounter something smaller than your max, sift it down <--
# if you enc someth greater than your max, append it