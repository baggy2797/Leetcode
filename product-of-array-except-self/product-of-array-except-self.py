class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length
        
        for i in range(1,length):
            left[i] = left[i-1]*nums[i-1]
        
        for i in range(length-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        
        for i in range(length):
            left[i] = left[i]*right[i]
        
        return (left)
        