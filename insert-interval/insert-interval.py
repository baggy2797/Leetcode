class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:return [newInterval]
        intervals.append(newInterval)
        intervals.sort()
        output = []
        
        for i in range(len(intervals)):
            if output and output[-1][1] >= intervals[i][0]:
                output[-1][1] = max(output[-1][1],intervals[i][1])
            else:
                output.append(intervals[i])
        return (output)
        