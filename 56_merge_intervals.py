# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
#  --- [1, 6] ---
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# 9:29
def merge(intervals):
    i = 0
    # import pdb; pdb.set_trace()
# 0       1
#     0        1
    while i < len(intervals) - 1:
        int1, int2 = intervals[i], intervals[i + 1]
        if ( int2[1] >= int1[1] >= int2[0] ) or (int1[1] >= int2[1] >= int1[0] ):
            extremes = intervals[i] + intervals[i + 1]
            newInterval = [min(extremes), max(extremes)]
            intervals[i], intervals[i + 1] = newInterval, newInterval
        i += 1
    return intervals
            
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