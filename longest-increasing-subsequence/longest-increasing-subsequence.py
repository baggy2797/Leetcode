class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        
        for i in range(length-1,-1,-1):
            for j in range(i+1,length):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)