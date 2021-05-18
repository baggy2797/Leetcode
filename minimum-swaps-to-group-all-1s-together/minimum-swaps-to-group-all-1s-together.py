class Solution:
    def minSwaps(self, data: List[int]) -> int:
        windowSize = sum(data)
        countOne = maxOne = 0
        left = right = 0
        
        while right < len(data):
            countOne+= data[right]
            right+=1
            
            if right - left > windowSize:
                countOne -= data[left]
                left+=1
            maxOne = max(maxOne,countOne)
            
        return windowSize - maxOne
                
        