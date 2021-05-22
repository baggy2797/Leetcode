class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minimal,self.maximal = [],[]

    def addNum(self, num: int) -> None:
        if len(self.minimal) == len(self.maximal):
            heappush(self.maximal,-heappushpop(self.minimal,-num))
        else:
            heappush(self.minimal,-heappushpop(self.maximal,num))

    def findMedian(self) -> float:
        if len(self.minimal) == len(self.maximal):
            return float(self.maximal[0] - self.minimal[0])/2.0
        else:
            return float(self.maximal[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()