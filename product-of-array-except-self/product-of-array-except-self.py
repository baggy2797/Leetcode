class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        length = len(nums) #O(n)
        if length == 2:
            return [nums[1],nums[0]]
        leftProduct = [1 for i in range(length)] #O(n)
        
        product = 1
        for i in range(1,length): #O(n)
            product *= nums[i-1]
            leftProduct[i] = product
        
        product = 1
    
        for i in range(length-2,-1,-1):
            product *= nums[i+1]
            leftProduct[i] = product*leftProduct[i]
        
        return leftProduct