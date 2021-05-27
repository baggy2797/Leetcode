class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None:return 0
        length = len(nums)
        # dp = [0]*(length+1)
        
        robNextPlusOne = 0
        robNext = nums[length-1]
        
        for i in range(length-2,-1,-1):
            current = max(robNext,robNextPlusOne+nums[i])
            robNextPlusOne = robNext
            robNext = current
        return robNext