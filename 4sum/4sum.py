class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        result = {}
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                start = j+1
                end = len(nums)-1
                
                while start < end:
                    temp = nums[i]+nums[j]+nums[start]+nums[end]
                    if temp == target:
                        
                        result[nums[i],nums[j],nums[start],nums[end]] = 0
                        start = start + 1
                        end = end - 1
                    
                    elif temp < target:
                        start = start + 1
                    else:
                        end = end - 1
        
        return (result.keys())
        
        
    
                
                
                            
        