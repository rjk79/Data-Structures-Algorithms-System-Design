import collections
class TweetCounts:

    def __init__(self):
        self.times = collections.defaultdict(list)

    def recordTweet(self, tweetName, time):
        self.times[tweetName].append(time)
        
    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        freqs = {
            "minute": 60,
            "hour": 3600,
            "day": 86400,
        }
        
        userTimes = self.times[tweetName]
        userTimes.sort()
        res = []
        startIdx = 0
        while startIdx < len(userTimes) and userTimes[startIdx] < startTime: #find where times start being equal or greater
            startIdx += 1
        endIdx = 0
        while endIdx < len(userTimes) and userTimes[endIdx] <= endTime: #find 1st greater time's idx
            endIdx += 1
        i = startIdx
        while i < endIdx:
            j = i            
            while j < endIdx and userTimes[j] < userTimes[i] + freqs[freq]: #stay within one jump
                j += 1
            res.append(j - i)
            i = j
        return res

# inputs = ["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
# outputs = [[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

tweetCounts = TweetCounts()
tweetCounts.recordTweet("tweet3", 0)
tweetCounts.recordTweet("tweet3", 60)
tweetCounts.recordTweet("tweet3", 10)
print(tweetCounts.getTweetCountsPerFrequency("minute","tweet3",0,59))
print(tweetCounts.getTweetCountsPerFrequency("minute","tweet3",0,60))
tweetCounts.recordTweet("tweet3",120)
print(tweetCounts.getTweetCountsPerFrequency("hour","tweet3",0,210))