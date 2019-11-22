# Input : arr[] = {1, 2, 1, 0, 1, 1, 0}, 
#            k = 4
# Output : 5

def atMostSum(arr, n, k): 
    currSum = 0
    maxLen = 0
    start = 0
    for end in range(n):
        currSum += arr[end]
        if currSum > k:
            currSum -= arr[start]
            start += 1
        maxLen = max(maxLen, end - start + 1)
    return maxLen
# window doesnt actually retain the best elements
# it only retains the size
print(atMostSum([1, 2, 1, 0, 1, 1, 0], 7, 4))