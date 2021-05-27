class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:return True
        seen = set()
        length = len(nums)
        
        for i in range(length):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True
        return False