class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:return [[]]
        output = []
        intervals.sort()
        # print(intervals)
        for i in range(len(intervals)):
            if output and output[-1][1] >= intervals[i][0]:
                start,end = output.pop()  
                output.append([start,max(intervals[i][1],end)])
            
            else:output.append(intervals[i])
            
        return (output)
                
        
            
            
        
    
        