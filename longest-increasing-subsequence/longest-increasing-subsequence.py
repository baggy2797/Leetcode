class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None:return 0
        length = len(nums)
        dp = [0]* length
        dp[0] = 1
        maxAns = 1
        for i in range(length):
            maxval = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxval = max(maxval,dp[j])
            
            dp[i] = maxval+1
            maxAns = max(maxAns,dp[i])
        return maxAns