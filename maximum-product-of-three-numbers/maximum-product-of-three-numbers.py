class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[0]*nums[1], nums[-1]*nums[-2]*nums[-3])
#         maxi = (-1)*sys.maxsize
        
#         for i in range(len(nums)):
            
#             l,r = i+1,len(nums)-1
            
#             while l<r:
                
#                 temp = nums[i]*nums[l]*nums[r]
                
#                 if  temp > maxi:
#                     maxi = temp
                
#                 l = l+1
#                 r = r-1
        
#         return (maxi)
        
                