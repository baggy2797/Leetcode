class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:return intervals
        length = len(intervals)
        
        output = []
        intervals.sort()
        for interval in intervals:
            if output and output[-1][1] >= interval[0]:
                start,end = output.pop()
                end = max(end,interval[1])
                start = min(start,interval[0])
                output.append([start,end])
            else:
                output.append(interval)
        
        return (output)