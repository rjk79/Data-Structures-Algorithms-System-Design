def findMin(nums):
    l = 0
    r = len(nums) -1
    while l < r:
        mid = (l + r) //2
        # print(mid)
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[l] > nums[mid]:
            r = mid 
        else:
        # nums[r] < nums[mid]:
            l = mid + 1

print(findMin([3,4,5,1,2]))
#1

print(findMin([4,5,6,7,0,1,2]))
#0

print(findMin([4,5,6,7]))
#4

# if we are looking at a given el, by looking at arr.first,
# we can tell whether pivot is L or R of us
# f(el, arr.first) => dir of pivot