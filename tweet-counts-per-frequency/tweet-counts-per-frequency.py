class TweetCounts:

    def __init__(self):
        self.storage = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.storage:self.storage[tweetName]= [time]
        else:self.storage[tweetName].append(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        freqInSeconds = {"minute":60,"hour":3600,"day":86400}
        
        times = self.storage[tweetName]
        secs = freqInSeconds[freq]
        size = (endTime - startTime) //secs  + 1
        result = [0] * size
        
        
        for i in times:
            if startTime <= i <= endTime:
                idx = int((i-startTime)/secs)
                result[idx]+=1
        return result

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)