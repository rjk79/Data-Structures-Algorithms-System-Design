# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
#  --- [1, 6] ---
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# 9:29
def merge(intervals):
    res = []
    # sort by lower bound
        intervals.sort(key = lambda interval : interval[0])
        for curr in intervals:
            if not res: #if its the 1st thing:
                res.append(curr)
            else:
                last = res[-1]
# because theyre sorted, you know the curr interval isnt completely before the res[-1] one
# if last thing's upper >= current things lower:
#   then modify the last thing's upper to be the max of the 2
                if last[-1] >= curr[0]:
                    res[-1] = [last[0], max(last[-1], curr[-1])]
                else:
                    res.append(curr)
        return res
            
# iter over each
#   iter over each other
#       find range of both
#       if anything in the range is included in the other range:
#           then find min and max of the 4 vals and create new 

# assuming intervals are at least 1
# better method:
#   if 1st things [1] > 2nd thing's [0]
#   || vice-versa
#   then find min and max of the 4 vals and create new 
#   set intervals[i] = 0 and intervals[i + 1] = newInterval

print (merge([[1,3],[2,6],[8,10],[15,18]]))