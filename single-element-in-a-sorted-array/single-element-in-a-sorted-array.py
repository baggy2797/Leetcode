class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        left,right = 0,length-1
        
        while left <= right:
            mid = (left + right)//2
            
            if mid == length -1 or mid == 0:
                return nums[mid]
            
            if nums[mid-1] !=nums[mid] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            
            elif nums[mid-1]!=nums[mid] and mid%2==0:
                left = mid+1
            elif nums[mid-1]!=nums[mid] and mid%2!=0:
                right = mid
            elif nums[mid+1]!=nums[mid] and mid%2==0:
                right = mid
            elif nums[mid+1]!=nums[mid] and mid%2!=0:
                left = mid+1