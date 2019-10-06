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