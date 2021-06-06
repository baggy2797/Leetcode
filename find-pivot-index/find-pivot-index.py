class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        1 7 3 6 5 6
      l 0   1   8   11  17  22
      r 27  20  17  11   6   0
                    res    
        '''
        length = len(nums)
        rightSum = sum(nums)
        leftSum = 0
        
        for i in range(length):
            rightSum -= nums[i]
            
            if leftSum ==rightSum:
                return i
            leftSum+= nums[i]
        
        return -1