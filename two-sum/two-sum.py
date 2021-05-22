class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.quickCheck = {}
        length = len(nums)
        
        for i in range(length):
            self.quickCheck[nums[i]] = i
        
        for i in range(length):
            search = target - nums[i]
            if search in self.quickCheck and self.quickCheck[search]!= i:
                return [i,self.quickCheck[search]]
        