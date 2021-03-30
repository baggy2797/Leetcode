class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new = []
        for height in heights:
            new.append(height)
            
        new.sort()
        
        for i in range(len(new)):
            new[i] = (new[i]-heights[i])
        count = 0
        for i in new:
            if i!=0:
                count+=1
        return(count)