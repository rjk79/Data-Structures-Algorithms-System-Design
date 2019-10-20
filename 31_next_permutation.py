def nextPermutation(nums):
    selectedPlace = float('-inf')
    # start at 2nd to last thing
    for i in reversed(range(len(nums)-1)):
        # import pdb; pdb.set_trace()
        # print(nums[i])
        if nums[i] < nums[i+1]: 
            selectedPlace = i 
            break
    print (selectedPlace)
    if selectedPlace: return nums.sort()
    nextHighestPlace = None
    for j in range(selectedPlace + 1, len(nums)):
        if nums[j] > nums[selectedPlace]:
            if not nextHighestPlace:
                nextHighestPlace = j
            elif nextHighestPlace > nums[j]:
                nextHighestPlace = j
    nums[nextHighestPlace], nums[selectedPlace] = nums[selectedPlace], nums[nextHighestPlace]
    nums[selectedPlace+1:] = sorted(nums[selectedPlace+1:])

# arr = [1, 2, 3]
# print nextPermutation(arr)
# print (arr) #132

arr2 = [1, 2]
nextPermutation(arr2)
print (arr2)
