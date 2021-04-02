class Solution:
    def countBits(self, num: int) -> List[int]:
        res,count = [],0
        
        for i in range(num+1):
            while i !=0:
                i = i & (i-1)
                count+=1
            res.append(count)
            count = 0
        return (res)
            
            
        