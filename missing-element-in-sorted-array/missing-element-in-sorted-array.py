class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def calculateMissings(i):
            return nums[i] - nums[0] - i
        
        l,r = 0,len(nums)
        
        while l < r:
            mid = (l + r)//2
            if calculateMissings(mid) < k: 
                l=mid + 1
            else:
                r=mid
            
        return nums[0]+k+l -1

            
            
        
            
            