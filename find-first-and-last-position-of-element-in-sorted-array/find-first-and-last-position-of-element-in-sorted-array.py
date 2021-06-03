class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    #FIND THE ELEMEENT  from the lower side
    #find the element form the upper side
    #if both not found return [-1,-1]
    #if found return the indices of the found the elements 
        
        if not nums:return [-1,-1]
        self.length = len(nums)
 
        def findLow(target):
            low,high = 0,self.length-1
            while low < high:
                mid = (high + low) //2
                
                if target <= nums[mid]: high = mid
                # elif nums[mid] <= target:left = mid
                else:low = mid +1
            return high if nums[high] == target else -1
        
        def findHigh(target):
            low,high = 0,self.length-1
            
            while low < high:
                mid = (high + low) //2+1
                
                if target >= nums[mid]: low = mid
                else: high = mid-1
            return low if nums[low] == target else -1
        
        return [findLow(target),findHigh(target)]
        
        
        