class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        length = len(nums)
        for i in range(length):
            if nums[i]!=0:
                nums[i],nums[left] = nums[left],nums[i]
                # print(nums)
                left+=1            