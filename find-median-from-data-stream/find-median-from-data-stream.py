class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.length = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums,num)            

    def findMedian(self) -> float:
        # print(self.nums)
        # return 0
        # self.nums.sort()
        size = len(self.nums)
        if size%2==1:
            return self.nums[(size-1)//2]
        else:
            return (self.nums[size//2] + self.nums[(size//2)-1])/2
        # if len(self.nums) % 2 == 0:
        #     first_idx = len(self.nums)//2
        #     second_idx = first_idx-1
        #     return (self.nums[first_idx]+self.nums[second_idx])/2
        # else:
        #     idx = floor(len(self.nums)/2)
        #     return self.nums[idx]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()