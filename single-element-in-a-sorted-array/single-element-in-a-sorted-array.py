class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        left  = 0
        right = length-1
        
        while left < right:
            mid = ( left + right ) //2
            if nums[mid+1] == nums[mid] and (right-mid)%2 == 0:
                left = mid+2
            elif nums[mid+1] == nums[mid] and (right-mid)%2 != 0:
                right = mid-1
            elif nums[mid]== nums[mid-1] and (right-mid)%2 == 0:
                right = mid-2
            elif nums[mid]== nums[mid-1] and (right-mid)%2 != 0:
                left = mid+1
            else:
                return nums[mid]
        return nums[left]