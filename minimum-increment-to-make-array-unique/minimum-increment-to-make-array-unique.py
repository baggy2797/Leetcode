class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        
        steps = 0
        nextNum = 0
        
        for i in range(length):
            steps+= max(nextNum,nums[i]) - nums[i]
            nextNum = max(nums[i],nextNum)+1
        
        return steps