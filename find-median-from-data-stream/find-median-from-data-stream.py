class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.incomingData = []
        self.numberOfIncomingElements = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.incomingData,num)
        self.numberOfIncomingElements +=1
        
    def findMedian(self) -> float:

        if self.numberOfIncomingElements%2==1:
            return self.incomingData[(self.numberOfIncomingElements-1)//2]
        else:
            return (self.incomingData[self.numberOfIncomingElements//2] + self.incomingData[(self.numberOfIncomingElements//2)-1])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()