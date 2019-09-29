def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        #here we need a global wise list, each time we just append to the result
        rslt=[]
        
        def dfs(temp, idx):
            rslt.append(temp[:]) #pass temp[:] with shollow copy so that we wont change the result of rslt when temp is changed
            for i in range(idx, len(nums)):
                temp.append(nums[i])
                #backtrack
                dfs(temp, i+1)
                temp.pop()
                
                
        dfs([],0)
        return rslt

# [1, 2, 3]
# temp (each time it changes, its appended to rslt)
# []
# .append .append .append
# [1] -> [1, 2] -> [1, 2, 3]
# .pop
# [2, 3] [3] []
# .append .append 
# [2] [2, 3]
# .append 
# [3] 
