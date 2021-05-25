class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = nums[0]
        currMax  = nums[0]
        
        for i in range(1,len(nums)):
            currMax = max(currMax+nums[i],nums[i])
            globalMax = max(globalMax,currMax)
        return globalMax