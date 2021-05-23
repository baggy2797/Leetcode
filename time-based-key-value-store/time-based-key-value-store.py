class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storeTime = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storeTime[key].append((value,timestamp)) 

    def get(self, key: str, timestamp: int) -> str:
        temp = self.storeTime.get(key)
        
        length = len(temp)
        
        for i in range(length-1,-1,-1):
            if temp[i][1] <= timestamp:
                return temp[i][0]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)