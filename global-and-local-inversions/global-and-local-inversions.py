class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # length = len(nums)
        # localinversion = 0
        # globalinversion = 0
        
        return (all(abs(i-x) <=1 for i,x in enumerate(nums)))
        