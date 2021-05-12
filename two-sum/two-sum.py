class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.cache = {}
        length = len(nums)
        
        for idx,num in enumerate(nums):
            self.cache[num] = idx
        
        for i in range(length):
            search = target - nums[i]
            if search in self.cache and self.cache[search]!=i:
                return [i,self.cache[search]]