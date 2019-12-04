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