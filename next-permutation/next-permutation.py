class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i > -1:
            if nums[i] < nums[i+1]:
                pivot = j = i+1
                while j<len(nums) and nums[i] < nums[j]:
                    pivot = j
                    j += 1
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
            i-=1
        nums[i+1:] = nums[i+1:][::-1]
            