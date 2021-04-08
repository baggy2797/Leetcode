class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr = curr_min = maxx = nums[0]
        
        for i in range(1,len(nums)):
            # print(curr,curr*nums[i],nums[i])
            curr,curr_min = max(nums[i], curr * nums[i],curr_min * nums[i]),min(nums[i], curr * nums[i],curr_min * nums[i])
            maxx = max(curr,maxx)
        
        return (maxx)

        
        
        