class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        if len(self.nums) % 2 == 0:
            first_idx = len(self.nums)//2
            second_idx = first_idx-1
            return (self.nums[first_idx]+self.nums[second_idx])/2
        else:
            idx = floor(len(self.nums)/2)
            return self.nums[idx]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()