class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [0]*(len(nums)+1)
        length = len(nums)
        
        dp[length]=0
        dp[length-1] = nums[length-1]
        for i in range(length-2,-1,-1):
            dp[i] = max(dp[i+1],dp[i+2]+nums[i])
        
        return dp[0]
        
                
    
