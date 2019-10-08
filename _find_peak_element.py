def findPeakElement(nums):
    # import pdb; pdb.set_trace()

    if len(nums) <= 1:
        return 0
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return 0
        elif nums[1] > nums[0]:
            return 1
    # need to convert to int outside of VSC
    midIdx = int(len(nums) / 2)
    mid = nums[midIdx]
    left = nums[midIdx - 1] or float('-inf')
    right = nums[midIdx + 1] or float('-inf')
    if mid > left and mid > right: 
        return midIdx
    elif mid < left: #go left
        return findPeakElement(nums[:midIdx])
    elif mid < right: #go right
    # classic + 1
        return midIdx + findPeakElement(nums[midIdx + 1:]) + 1
    else:
        return findPeakElement(nums[:midIdx])



print (findPeakElement([1, 2, 3, 1]))
# 2
print (findPeakElement([1, 2, 1, 3, 5, 6, 4]))
# 1, 5

