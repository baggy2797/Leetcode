class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 1:return 1
            if nums[0] == 0:return 0
        
        
        for i in range(1,len(nums)):
            if nums[i] == 0:
                continue
            elif nums[i] == 1:
                nums[i] = nums[i-1]+1
        return max(nums)
        
        
        
            
        
        