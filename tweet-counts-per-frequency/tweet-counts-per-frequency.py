class TweetCounts:

    def __init__(self):
        self.tweetStorage = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweetStorage:
            self.tweetStorage[tweetName] = [time]
        else:
            self.tweetStorage[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        times = self.tweetStorage[tweetName]
        temp = freq.lower()
        size ,secs = 0,0
        if temp == "minute":
            secs = 60
            size = (endTime -startTime)/secs + 1
            
        elif temp == "hour":
            secs = 3600
            size = (endTime -startTime)/secs + 1
            
        elif temp == "day":
            secs =86400
            size = (endTime -startTime)/secs + 1
            
        r = [0] * int(size)
        
        for i in times:
            if startTime <= i and i<= endTime:
                index = int((i-startTime)/secs)
                r[index] +=1
        return r
        
        
        
# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)