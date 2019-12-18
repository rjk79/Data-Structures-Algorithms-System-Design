# Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , determine if a person could attend all meetings.

# For example,
# Given [ [0, 30], [5, 10], [15, 20] ],
# return false.

def meetingRooms(times):
    times.sort()
    # last thing's last time might not be the max so find max of end times
    maxTime = max([time[-1] for time in times])
    dp = [0 for _ in range(maxTime)]
    for time in times:
        for i in range(time[0], time[1]):
            dp[i] += 1
    for entry in dp:
        if entry > 1: return False
    return True

print(meetingRooms([ [0, 30], [5, 10], [15, 20] ]))

def meetingRooms2(times):
    times.sort()
    # last thing's last time might not be the max so find max of end times
    maxTime = max([time[-1] for time in times])
    dp = [0 for _ in range(maxTime)]
    for time in times:
        for i in range(time[0], time[1]):
            dp[i] += 1
    return max(dp)
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
# find the minimum number of conference rooms required.

print (meetingRooms2([[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]])) #2

    starts = []
    ends = []
    for i in intervals:
        starts.append(i.start)
        ends.append(i.end)
    
    starts.sort()
    ends.sort()
    s = e = 0
    numRooms = available = 0
    while s < len(starts):
        # this cond is always met 1st since 1st meeting must START
        if starts[s] < ends[e]: #must go thru the events in order (free uppings and bookings)
            if available == 0:
                numRooms += 1 #need to build another room
            else:
                available -= 1 # reserve a room
                
            s += 1
        else:
            available += 1 # a room got freed up
            e += 1
    
    return numRooms

starts = [2  36 9  16 4]
[2 4 |9 16 36]
ends =   [15 45 29 23 9]
[9 |15 23 29 45]
s = 0 1 2 3
e = 0 1
numRooms = 0 1 2
available = 0 1 0 #draw from avail when we can
