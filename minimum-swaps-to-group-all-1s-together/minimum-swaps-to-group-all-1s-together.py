class Solution:
    def minSwaps(self, data: List[int]) -> int:
        #time complexity : O(2n) = O(n)
        #space complexity : O(1)
        
        if not data:return 0
        
        globalMin = 0
        length = len(data)
        # count the number of ones
        CountOfOnes = sum(data) #O(n)
        #since this is going to be the data frame(windowsize)
        windowSize = CountOfOnes
        #check by going on sliding the window through the array till the last element matches the window end and no further
        left = 0
        right = 0
    
        count = 0
        while right < length:
            count += data[right]
            right+=1
            if right - left > windowSize:
                count-=data[left]
                left+=1
        
            globalMin = max(globalMin,count)
            
        return windowSize - globalMin
        #keeping a global Minimum to be comapred everytime so as to get the required minimum
                
        