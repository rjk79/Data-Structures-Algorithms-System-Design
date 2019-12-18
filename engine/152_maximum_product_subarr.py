def maxProduct(nums):
    reverse = [i for i in reversed(nums)]
    for i in range(1, len(nums)):
        nums[i] *= nums[i-1]
        reverse[i] *= reverse[i-1]
    return max(nums + reverse)

print (maxProduct([2, 3, -2, 4]))