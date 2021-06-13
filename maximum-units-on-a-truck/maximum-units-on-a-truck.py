class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[-1])
        maxUnits = 0
        currSize = 0
        for numBox,unit in boxTypes:
            maxUnits += unit * min(truckSize-currSize,numBox)
            currSize += min(truckSize - currSize,numBox)
        return maxUnits