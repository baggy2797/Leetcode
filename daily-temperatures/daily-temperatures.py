class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        length = len(temperatures)
        res = [0]* length
        stack = []
        
        for idx,value in enumerate(temperatures):
            while stack and stack[-1][0] < value:
                stackTopIndex = stack.pop()[1]
                count = idx - stackTopIndex
                res[stackTopIndex] = count
            
            stack.append((value,idx))
        return res
                