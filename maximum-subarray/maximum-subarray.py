class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
                temp = maxi + nums[i]
                maxi = max(temp,nums[i])
                max_sum = max(max_sum,maxi)
            
        return(max_sum)