class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        length = len(nums)
        if not nums:
            return 0
        if length == 1:
            return 1
        if length == 2:
            if nums[0]+1 == nums[1] or nums[1]+1 == nums[0]:
                return 2
            else:
                return 1
        maxLength = 1
        for i in range(length):
            if nums[i]+1 in hashSet:
                j = nums[i]
                length = 0
                while j in hashSet:
                    j+=1
                    length+=1
                maxLength = max(maxLength,length)
        return maxLength
                
                
                
                
                
                
                
                
                
                
                
            # if (nums[i]+1) in hashSet:
            #     j = i
            #     length = 0
            #     while j < length and nums[j]+1 in hashSet:
            #         j+=1
            #         length+=1
            #     print(length)
        
                    
        
            