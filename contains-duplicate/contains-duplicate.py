class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        length = len(nums)
        for i in range(length):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = seen.get(nums[i],0)+1
                