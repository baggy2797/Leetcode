class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        res = nums[0]
        for i in range(1,length):
            res ^= nums[i]
        
        return res