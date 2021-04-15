class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == []:
            return 1
        if max(nums) < 1:
            return 1
        else:
            new = []
            for i in nums:
                if i > 0:
                    new.append(i)
            count = 1
            while count in nums:
                count = count + 1
            return count