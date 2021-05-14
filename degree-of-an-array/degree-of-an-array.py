class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        length = len(nums)
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        maxKey,maxVal = 0,0
        for key,value in freq.items():
            if value > maxVal:
                maxVal = value
                maxkey = key
        
        check = []
        for i in freq:
            if freq[i] == maxVal:
                check.append(i)
        
        minlength = float("inf")
        
        for num in check:
            left = 0
            #check the leftmost appearance of num
            for i in range(length):
                if nums[i] == num:
                    left = i
                    break
            right = 0
            #check the rightmost appearance of num
            for i in range(length-1,-1,-1):
                if nums[i] == num:
                    right = i
                    break
            #find the length
            temp = right - left + 1
            #compare the length with minlength
            if temp < minlength:
                minlength = temp
                
        return minlength