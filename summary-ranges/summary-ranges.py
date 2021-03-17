class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i=0
        while i<len(nums):
            r = i+1
            new = "" + str(nums[r-1])
            
            while r<=len(nums)-1 and nums[r]-nums[r-1]==1:
                print(nums[r-1],nums[r])
                # l = l+1
                r = r+1
                    
            if int(new) == nums[r-1]:
                res.append(str(nums[r-1]))
            else:
                new  = new +"->"+ str(nums[r-1])
                if new not in res:
                    res.append(new)
                    
            i = r
        return res
            
                
            
                
        
        