class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return []
        self.fetcher = {}
        length = len(nums)  #O(n)
        
        for i in range(length):  #O(n)
            self.fetcher[nums[i]] = i
            
        for i in range(length):    #O(n)
            search = target - nums[i]
            
            if search in self.fetcher and self.fetcher[search]!=i: #O(1) lookup and checking for equality
                return [i,self.fetcher[search]]