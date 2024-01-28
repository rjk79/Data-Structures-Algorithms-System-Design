def longestConsecutive(nums):
        numSet = set(nums)
        bestCount = 0
        for num in nums:
# only do checks for things that havent been visited before
            if num - 1 not in numSet:
                currNum = num
                count = 1
                while (currNum + 1) in numSet:
                    count += 1
                    currNum += 1
                if count > bestCount: bestCount = count 
        return bestCount

a = [100,4,200,1,3,2]
print(longestConsecutive(a))