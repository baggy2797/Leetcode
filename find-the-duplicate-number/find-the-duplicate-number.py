class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        seen = set()
        
        for i in range(length):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return nums[i]
        