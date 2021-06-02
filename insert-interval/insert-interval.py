class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals is None:
            return [[newInterval]]
        intervals.append(newInterval)
        output = []
        intervals.sort()
        length = len(intervals)
        
        
        for i in range(length):
            if output and output[-1][1] >= intervals[i][0]:
                start,end = output.pop()
                output.append([start,max(end,intervals[i][1])])
            else:
                output.append(intervals[i])
                
        return (output)
        
        