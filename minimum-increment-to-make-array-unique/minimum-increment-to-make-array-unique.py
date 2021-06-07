class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        s1 = sum(nums)
        n = len(nums)
        for i in range(1, n): 
            if nums[i] <= nums[i - 1]:
                nums[i] = max(nums[i], nums[i-1]+1)
        s2 = sum(nums)
        return s2 - s1