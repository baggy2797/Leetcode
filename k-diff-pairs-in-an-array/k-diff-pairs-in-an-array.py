class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 1
        length = len(nums)
        count = 0

        while left < length and right < length:
            if left == right or nums[right] - nums[left] < k:right+=1
            elif nums[right] - nums[left] > k:left+=1
            else:
                left+=1
                count+=1
                while left < length and nums[left] == nums[left-1]:
                    left+=1
            
        return count