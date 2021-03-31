class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        new = self.timeMap.get(key,None)
        if new is None: 
            return ""
        i = bisect.bisect(new,(timestamp,chr(127)))
        
        return new[i-1][1] if i else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)