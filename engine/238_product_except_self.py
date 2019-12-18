def productExceptSelf(nums):
    leftProds = [1 for i in range(len(nums))]
    for i in range(1, len(nums)):

        leftProds[i] = nums[i-1] * leftProds[i-1]
    rightProds = [1 for i in range(len(nums))]
    for i in reversed(range(len(nums)-1)):
        # import pdb; pdb.set_trace()
        rightProds[i] = nums[i+1] * rightProds[i + 1]
    for i in range(len(nums)):
        nums[i] = leftProds[i] * rightProds[i]
    # print(leftProds)
    # print(rightProds)
    return nums

print(productExceptSelf([1, 2, 3, 4]))
# 1  2  3  4

# 1  1  2  6
# 24 12 4  1
# 24 12 8  6