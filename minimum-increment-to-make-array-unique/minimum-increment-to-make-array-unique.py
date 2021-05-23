class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        nextNum = float('-inf')
        steps = 0
        
        for num in nums:
            steps += max(nextNum,num) - num
            nextNum = max(num,nextNum)+1
        return steps            
        
        