class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1]*length
        
        for i in range(1,length):
            for j in range(0,i):
                if nums[i] > nums[j] and dp[i] < dp[j] +1:
                    dp[i] = dp[j]+1
        return max(dp)