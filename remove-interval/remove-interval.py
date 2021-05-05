class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals: 
            if interval[0] < toBeRemoved[0]: 
                res.append([interval[0], min(toBeRemoved[0], interval[1])])
            if toBeRemoved[1] < interval[1]: 
                res.append([max(interval[0], toBeRemoved[1]), interval[1]])
        return res 