class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target-nums[i]
            if a in nums and i!=nums.index(a):
                return([i,nums.index(a)])