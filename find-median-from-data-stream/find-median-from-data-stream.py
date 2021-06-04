class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = [] # to store all the greater values -1
        self.maxHeap = [] # to store all the lesser values  +1
        # heapq.heapify(self.minHeap)
        # heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        #add the number first to the maxHeap
        heappush(self.minHeap,-num)
        heappush(self.maxHeap,-heappop(self.minHeap))
        
        #if length(maxHeap) > length(minHeap)
        if len(self.maxHeap) > len(self.minHeap):
            heappush(self.minHeap,-heappop(self.maxHeap))
            
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (self.maxHeap[0]-self.minHeap[0])/2
        else:
            return float(-self.minHeap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()