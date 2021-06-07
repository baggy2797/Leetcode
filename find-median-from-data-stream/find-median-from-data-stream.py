class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = [] # store all the smaller values here 
        #send all the value as negative of themselves (above)
        
        self.minHeap = [] # store all the larger values here  
        
    def addNum(self, num: int) -> None:
        heappush(self.minHeap,-num) #put the number in the pool of bigger numbers
        heappush(self.maxHeap,-heappop(self.minHeap)) # pop the smallest number from that pool and push it to the smaller numbers
        
        #check if the length of minHeap < maxHeap then append a number from maxHeap to minHeap
        if len(self.minHeap) < len(self.maxHeap):
            heappush(self.minHeap,-heappop(self.maxHeap))
            
    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return -self.minHeap[0]
        else:return (self.maxHeap[0] - self.minHeap[0]) /2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()