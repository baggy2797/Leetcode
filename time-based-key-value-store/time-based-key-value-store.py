class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Time[key] += [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.Time:
            return ""
        target = self.Time[key]
        i = len(target)-1
        
        while i>=0 and target[i][0] > timestamp:
            i-=1
        return target[i][1] if i>=0 else ""
                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)