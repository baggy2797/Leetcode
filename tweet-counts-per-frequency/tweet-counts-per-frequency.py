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
        
        size = 0
        secs = 0
        
        if freq == "minute":
            secs = 60
            size = (endTime-startTime)/ 60 + 1
        elif freq == "hour":
            secs = 3600
            size = (endTime-startTime)/ 3600 + 1
        else:
            secs = 86400
            size = (endTime-startTime)/ 86400 + 1
        
        
        results = [0]*int(size)
        
        for i in times:
            if startTime <= i <= endTime:
                idx = int((i-startTime)/secs)
                results[idx] +=1
            
        return results
            


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)