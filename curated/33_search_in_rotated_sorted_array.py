class Solution:
    def search(self, nums: List[int], target: int) -> int:
#       boilerplate b-search
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = int((lo + hi) / 2)
            if (nums[mid] < nums[0]) == (target < nums[0]):
                num = nums[mid] 
# mid and target are on diff "sides" 
# the split caused by rotation denotes "sides"
            else:
                if target < nums[0]:
                    # target is on right "side"
                    # allows us to look right in next step (lo = mid + 1)
                    num = float('-inf') 
                else:
                    # target is on left "side"
                    # allows us to look left in next step (hi = mid)
                    num = float('inf')
            if num < target:
                lo = mid + 1
            elif num > target:
                hi = mid
            else:
                return mid
        return -1
# Given:
# asc----> asc---->
# target mid ---> ---->   reg
# -----> target mid ---> reg