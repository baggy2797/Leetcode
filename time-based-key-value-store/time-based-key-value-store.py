class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        new = self.time.get(key,None)
        if new is None: 
            return ""
        i = len(new)-1
        while i >= 0 and new[i][1] > timestamp:
            i -= 1
        return new[i][0] if i >= 0 else ""
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)