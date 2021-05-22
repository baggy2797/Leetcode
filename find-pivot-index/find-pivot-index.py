class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = sum(nums)
        
        
        for i in range(length):
            right-= nums[i]
            
            if left == right:
                return i
            
            left+= nums[i]
        return -1
                
        