def rob(nums):
        if len(nums) == 1: return nums[0]
        if len(nums) == 0: return 0
        
        visitFirst = [0 for i in range(len(nums))]
        visitSecond = [0 for i in range(len(nums))]
        
        visitFirst[0] = nums[0]
        visitFirst[1] = 0
        
        visitSecond[0] = 0
        visitSecond[1] = nums[1]
        import pdb; pdb.set_trace()

        for i in range(2, len(nums)):
            visitFirst = max(visitFirst[i - 1], visitFirst[i - 2] + nums[i])
            visitSecond = max(visitSecond[i - 1], visitSecond[i - 2] + nums[i])


        return max(visitFirst[len(nums) - 2], visitSecond[len(nums) - 1])
        
print (rob([1,2,3,1]))