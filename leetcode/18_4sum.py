def fourSum(nums, target):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        subs = three_sum(nums[i+1:], target-nums[i])
        res += subs
    return res
def three_sum(nums, target):
        res = []
        i = 0
        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1
            while left != right:

                if nums[i] + nums[left] + nums[right] == target:
                    sub = [nums[i], nums[left], nums[right]]
    #               removed the sort and !include to decrease run time
                    res.append(sub)
    #               skip duplicates
                    oldLeft = left
                    while nums[oldLeft] == nums[left] and left != right:
                        left += 1

                    oldRight = right
                    while nums[oldRight] == nums[right] and left != right:
                        right -= 1
                    
    #               end skipping  
                elif nums[i] + nums[left] + nums[right] > target:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < target:
                    left += 1

    #       skip dups
            oldI = i
            while nums[oldI] == nums[i]:
                i += 1
        return res

# print (three_sum([-1, 0, 1, 2, -1, -4], 0))
print (fourSum([1, 0, -1, 0, -2, 2], 0))