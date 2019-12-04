# [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]

# order doesnt matter so recur calls form triangle
# AKA no repeats

# basic format of backtracking

# res = []
# def recurse(curr = [], currIdx)
#       res.append
#       for loop starting at currIdx
#               curr.append
#               recurse
#               curr.pop
# return res
def subsets(nums):
        res = []
        def recurse(curr, idx):
# base case
# append to res
# for loop
# recurse
# undo
# NEED TO MAKE SHALLOW COPY!! can do : or ::
            res.append(curr[:])
            # if rem == []:
            #     return 
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                recurse(curr, i + 1)
                curr.pop()
            
        recurse([], 0)    
        return res
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

print (subsets([1,2,3]))