class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp =  [0]*length
        dp[0] =1
        ans = 1
        for i in range(1,length):
            longest = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    longest = max(longest,dp[j])
            dp[i] = longest+1
            ans = max(ans,dp[i])
        return ans
        