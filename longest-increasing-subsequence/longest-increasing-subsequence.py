class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        10 9 2 5 3 7 101 18
         1 1 1 2 2 3 4   4
         4
        
        
        """
        length = len(nums)
        dp = [1]* length
        
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1,dp[i])
                    
        return max(dp)