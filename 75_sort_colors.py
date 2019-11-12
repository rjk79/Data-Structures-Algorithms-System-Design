def sortColors(nums):
      
        maxRange = len(nums)
        i = 0
        while i < maxRange:
            curr = nums[i]
            if curr == 2:
                nums = nums[:i] + nums[i+1:]
                nums.append(curr)
                maxRange -= 1
            elif curr == 0:
                nums = nums[:i] + nums[i+1:]
                nums = [curr] + nums
                i += 1
            else: #1
                i += 1
            # import pdb; pdb.set_trace()

        

arr = [2,0,2,1,1,0]

sortColors(arr)

print arr

def sortColors(self, nums):
    i = j = 0
    for k in xrange(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
nums 2 0 2 1 1 0
     0 2
i 0 1
j 0 1
k 0 1
# v is old value
v 2 0