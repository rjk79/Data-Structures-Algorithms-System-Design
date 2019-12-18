def nextPermutation(nums):
    selectedPlace = float('-inf')
    # start at 2nd to last thing and iters down
    for i in reversed(range(len(nums)-1)):
        # 4 5
        if nums[i] < nums[i+1]: 
            selectedPlace = i 
            break
    print (selectedPlace)
    if selectedPlace: return nums.sort()
    nextHighestPlace = None
    # look at nums to the right
    for j in range(selectedPlace + 1, len(nums)):
        if nums[j] > nums[selectedPlace]:
            if not nextHighestPlace:
                nextHighestPlace = j
                # if el is greater selected el BUT LESS than our best lowest, it becomes our best
            elif nextHighestPlace > nums[j]:
                nextHighestPlace = j
                # swap
    nums[nextHighestPlace], nums[selectedPlace] = nums[selectedPlace], nums[nextHighestPlace]
    nums[selectedPlace+1:] = sorted(nums[selectedPlace+1:])

arr = [1, 2, 3]
print nextPermutation(arr)
print (arr) #132

arr2 = [1, 2]
nextPermutation(arr2)
print (arr2)
