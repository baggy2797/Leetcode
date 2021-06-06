class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
#         length = len(nums)
#         left = 0
#         right = length-1
        
#         while left <= right:
#             if nums[left] is not 1 and nums[right] is not 1:
#                 if nums[left] == 0:
#                     left+=1
                
#                 if nums[right] == 2:
#                     right-=1
                 
#                 elif nums[left] == 2 or nums[right] == 1:
#                     nums[right],nums[left] = nums[left],nums[right]
#                     left+=1
#                     right-=1