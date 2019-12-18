def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target: return True
        import pdb; pdb.set_trace()
        while lo < mid and nums[lo] == nums[mid]:
            lo += 1
#           first half is ASC
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


# Given:
# asc----> asc---->
# target mid ---> ---->   reg
# -----> target mid ---> reg
# print (search([2,5,6,0,0,1,2], 0) == True)
# print (search([2,5,6,0,0,1,2], 3) == False)
# print (search([1,3,1,1], 3) == True)
print (search([1,3], 3) == True)

