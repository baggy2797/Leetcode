class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    right = mid
        #print(left, right)
        if left % 2 == 0:
            return nums[left]
        return nums[right]

#         length = len(nums)
        
#         left,right = 0 ,length-1
        
#         while left <= right:
#             mid = (left+right)//2
            
#             if nums[mid] == 0 or nums[mid] == length-1:
#                 return nums[mid]
#             elif nums[mid]!= nums[mid-1]!= nums[mid+1]:
#                 return nums[mid]
            
#             elif nums[mid]!= nums[mid-1] and mid%2 == 0:
#                 left = mid
                
#             elif nums[mid]!= nums[mid-1] and mid%2 != 0:
#                 right = mid-1
                
#             elif nums[mid]!= nums[mid+1] and mid%2 == 0:
#                 right = mid
                
#             elif nums[mid]!= nums[mid+1] and mid%2 != 0:
#                 left = mid+1
                
#             """
#             4  5
#             6  7    mid at 4 mid!=mid+1 and mid%2==0
            
#             5   6
#             6   7   mid at 5 and mid!=mid+1 and mid%2!=0
            
#             """