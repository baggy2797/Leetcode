class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        length = len(nums)
        for i in range(length):
            rightSum-=nums[i]
            if leftSum == rightSum:
                return i
            leftSum+=nums[i]
        return -1
            
            
            