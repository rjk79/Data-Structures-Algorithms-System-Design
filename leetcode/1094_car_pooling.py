def carPooling(trips, capacity):
        
# Alternate Solution:
        changes = []
        for change, start, end in trips:
#         pick up x at start, drop off x at end
            for x in [[start, change],[end, -change]]:
                changes.append(x)
#       doesnt work if specify 1st key as sorting param
        changes.sort()
    
        for x in changes:
            capacity -= x[1]
            if capacity < 0: return False
        return True
        
# WORKS
#         #, start, end
# never take partials

# sort by starts?
# iter over stops going east
# 
# make sure capacity never goes over
#         trips.sort(key = lambda a: a[1])
#         end = max([trip[2] for trip in trips])
#         dp = [0 for _ in range(end)]        
#         for trip in trips:
#             for i in range(trip[1], trip[2]):
#                 dp[i] += trip[0]
            
#         for place in dp:
#             if place > capacity: return False
#         return True
print (carPooling([[4,5,6],[6,4,7],[4,3,5],[2,3,5]], 13))
            