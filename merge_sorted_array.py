def merge(self, nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]: #assign the larger val to the end of nums1 (moving left)
            nums1[m+n-1] = nums1[m-1] 
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
# nums1 = [1,2,3,0,5,6]
# m = 3
# n = 3 2
# nums1[m-1] = 3
# nums2[n-1] = 6 5
# m+n-1 =      5 
# nums1[m-1] = 3

# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
