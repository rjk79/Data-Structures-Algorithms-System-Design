
def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2): #leftmost pointer
        print(i)
        if i > 0 and nums[i] == nums[i - 1]: #skip over duplicate i's
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                triplet = [nums[i], nums[l], nums[r]]
                res.append(triplet)

                while nums[l] == triplet[1] and l < r:#skip over duplicate l's
                    l += 1
                while nums[r] == triplet[2] and l < r:#skip over duplicate r's
                    r -= 1

    return res


#going to test pairs of numbers like 2 sum but with a shrinking left bound


# nums = [-1,0,1,2,-1,-4]
nums = [0, 0, 0]
print(threeSum(nums))
