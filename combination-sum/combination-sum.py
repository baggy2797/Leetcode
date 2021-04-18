class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        length = len(candidates)
        def backtrack(curr,currentSum,idx):
            if currentSum > target:
                return 
            if currentSum == target:
                result.append(curr)
                return 
            else:
                for i in range(idx,length):
                    backtrack(curr + [candidates[i]],currentSum + candidates[i],i)
        
        backtrack([],0,0)
        return result
        