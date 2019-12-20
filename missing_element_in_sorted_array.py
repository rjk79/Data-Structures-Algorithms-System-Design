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