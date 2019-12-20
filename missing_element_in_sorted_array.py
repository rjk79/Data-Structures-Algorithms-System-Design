def missingElement(nums, k):
    l,r=0,len(nums)-1
    
    while l<r:
        mid=(l+r+1)//2
        if nums[mid]-nums[0]-mid < k: #count the number of missing from the begining to mid point
            l=mid
        else:
            r=mid-1
        
    return nums[0]+k+l
A = [4,7,9,10]
K = 1
print(missingElement(A, K))
l =   0     #offset from start's value
r =   3 1 0
mid = 2 1
nums[mid]-nums[0]-mid < k
9 - 4 - 2 < 1       3 < 1   #missing too many nums (5, 6, 8) if using this range. AKA range is too big rel to the idx of "mid"

7 - 4 - 1 < 1       2 < 1   #missing too many nums still (5, 6)

=> 4 + 1 + 0 = 5
