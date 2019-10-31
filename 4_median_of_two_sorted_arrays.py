def findMedianSortedArrays(nums1, nums2):
# nums1 has len 'm' and is cut at 'i'
# nums2 has len 'n' and is cut at 'j'
    m = len(nums1)
    n = len(nums2)
    if m > n:
# swap everything if 1st arr is longer so that by default, 2nd arr is longer 
# prevents go neg when j = halflen - i
        nums1, nums2, m, n = nums2, nums1, n, m
# add one so by default, num of els on left side is more?
    half_len = (m + n + 1) / 2
# round up so that we know to take from lower array
    imin = 0
    imax = m
    while imin <= imax:
# sum of idxs == 1/2 of combined len of arrs
        i = (imin + imax) / 2
        j = half_len - i
# check for idx out of bounds (dont have to check j > 0 since this intrinsic checks that too) and then do diag check
        if i > 0 and nums1[i - 1] > nums2[j]:
# imin to imax denotes searchable range.
# change searchable range instead of 'i' directly so that we take logn time
# like (binary search)!!!
            imin = i + 1 #left window pointer moves
        elif j > 0 and nums2[j - 1] > nums1[i]:
            imax = i - 1 #right window pointer moves
        else:

# correct 'i' is found
# if 1st arr is partit such that there is nothing on left side
            if i == 0: left_max = nums2[j-1]
# if 2nd arr has nothing on left side
            elif j == 0: left_max = nums1[i-1]
            else: left_max = max(nums1[i-1], nums2[j-1])
                
            if i == m: right_min = nums2[j]
            elif j == n: right_min = nums1[i]
            else: right_min = min(nums1[i], nums2[j])
# even num of els
            # print(left_max, right_min)
            if (m + n) % 2 == 0:
                return (left_max + right_min)/2.0
# odd num of els  
            else:
                return left_max 

print(findMedianSortedArrays([1, 3], [2]))
# nums1 = [1, 3]
# nums2 = [2]
# ==>>2

# m = 2      1
# n = 1      2
# A = [1, 3] [2]
# B = [2]    [1, 3]

# imin      0   1
# imax      1
# half_len  2

# i = 0     1
# j = 2     1

# max_of_left = 2
# ==>> 2




#   item[i - 1] | item[i] 

# nums1 = [1, 2]
# nums2 = [3, 4]
# 2.5

# A = [1, 2]
# B = [3, 4]
# m = 2
# n = 2
# half_len = 2

# imin = 0  2
# imax = 2

# i = 1 2
# j = 1 0

# max_of_left = 2
# min_of_right = 3

# ==>> 2.5


# [1, 3, 8, 9,| 15]
# [7, 11,| 18, 19, 21, 25]
# ==>>11

# 1, 3, 7, 8, 9, 11, 15, 18, 19, 21, 25 