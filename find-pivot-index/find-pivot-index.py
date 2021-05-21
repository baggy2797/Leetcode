class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        leftSum = 0
        rightSum = sum(nums)
        for i in range(length):
            rightSum-= nums[i]
            if leftSum == rightSum:
                return i
            leftSum+= nums[i]
        return -1
            