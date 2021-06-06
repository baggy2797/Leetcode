class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        fetcher = {}
        
        for i in range(length):
            search = target - nums[i]
            if search in fetcher and fetcher[search]!=i:
                return [i,fetcher[search]]
            else:
                fetcher[nums[i]] = i
            
            