class LogSystem:

    def __init__(self):
        self.LogStorage = {}
        
    def put(self, id: int, timestamp: str) -> None:
        self.LogStorage[tuple(timestamp.split(':'))] =id

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        getGranularity = {"Year":1,"Month":2,"Day":3,"Hour":4,"Minute":5,"Second":6}
        index = (getGranularity[granularity])
        start = tuple(start.split(":")[:index])
        end = tuple(end.split(":")[:index])
        ans = []
        
        for t in self.LogStorage.keys():
            if start <= t[:index] <= end:
                ans.append(self.LogStorage[t])
        return ans
        

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)