class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            if len(nums)<2:
                return nums[-1]
            return max(nums[0],nums[1])
        
        dp = [0]*len(nums)
        dp[0],dp[1],dp[2] = nums[0],max(dp[0],nums[1]),max(dp[1],nums[2])
        
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1],dp[i-3]+nums[i])
        print(dp)
        return max(dp)
        
#         for i in range(2,len(nums)):
#             nums[i] = nums[i] + nums[i-2]
        
#         return max(nums[-1],nums[-2])