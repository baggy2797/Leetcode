class LogSystem:

    def __init__(self):
        self.logStorage = defaultdict(list)
    
    def put(self, id: int, timestamp: str) -> None:
        self.logStorage[timestamp] = id
        
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        level = {"Second":6,"Minute":5,"Hour":4,"Day":3,"Month":2,"Year":1}
        res = []
        idx = -1
        h1,h2 = start.split(":"),end.split(":")
        
        idx = level[granularity] - 1
        startTime = int("".join(h1[:idx+1]))
        endTime = int("".join(h2[:idx+1]))
        
        for key,value in self.logStorage.items():
            temp = "".join(key.split(":")[:idx+1])
            if startTime <= int(temp) <= endTime:
                res.append(value)
        
        return res
            
        
    

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)