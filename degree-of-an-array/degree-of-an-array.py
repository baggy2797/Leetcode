class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq,left,right = {},{},{}
        length = len(nums)
        
        for i in range(length):
            if nums[i] not in freq:
                freq[nums[i]] = 1
                left[nums[i]] = i
                right[nums[i]] = i
            else:
                freq[nums[i]] += 1
                # if i < left.get(nums[i]):left[nums[i]] = i 
                right[nums[i]] = i 
        
        #find the minLength
        minLength = float("inf")
        degreeList = max(freq.values())
        
        for num in freq:
            if freq[num] == degreeList:
                minLength = min(minLength,right[num] - left[num] + 1)
            
        if minLength == float("inf"):return 1
        return minLength