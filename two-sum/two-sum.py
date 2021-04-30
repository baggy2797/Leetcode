class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helperDictionary = {}
        length = len(nums)
        
        for i in range(length):
            helperDictionary[nums[i]] = i
            
        for i in range(length):
            search = target - nums[i]
            if search in helperDictionary and helperDictionary[search]!=i:
                return [i,helperDictionary[search]]