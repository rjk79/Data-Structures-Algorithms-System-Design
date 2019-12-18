def increasingTripletSubsequence(arr):
    if len(arr) < 3: return False
    left = 0
    while left < len(arr) - 2:
        if arr[left] < arr[left + 1] and arr[left + 1] < arr[left + 2]:
            return True
        left += 1
    return False


print (longestTripletSubsequence([1, 2, 3, 2]))
print (longestTripletSubsequence([5, 4, 2, 3]))

# start at a num. if the next one is larger, keep going
# if its smaller then move left to where right pointer is

# if len(arr) < 3: return False
# left = 0
# while left pointer < len of arr - 2:
#   if arr[left] < arr[right] and arr[left] < arr[right + 1]
#   left += 1  
# 
# return false